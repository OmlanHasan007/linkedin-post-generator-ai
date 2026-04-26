"""
linkedin_post_agent.py
----------------------
Standalone CLI agent for generating LinkedIn posts.
Can be used independently from the FastAPI backend for testing or scripting.
"""

import os
import asyncio
from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

if not BASE_URL or not MODEL_NAME:
    raise ValueError("Please set BASE_URL and MODEL_NAME in your .env file.")
if not API_KEY:
    raise ValueError("Please set API_KEY in your .env file.")

# ---------------------------------------------------------------------------
# Pydantic model
# ---------------------------------------------------------------------------
class LinkedInPost(BaseModel):
    """Structured representation of a LinkedIn post."""

    title: str = Field(description="Catchy headline for the post")
    content: str = Field(description="Main post body (2–4 paragraphs)")
    hashtags: List[str] = Field(description="Relevant hashtags (without the # symbol)")
    call_to_action: str = Field(description="Encouraging call to action")

    def format_post(self) -> str:
        """Return a ready-to-paste LinkedIn post string."""
        hashtag_str = " ".join(f"#{tag}" for tag in self.hashtags)
        parts = [self.title, self.content]
        if self.call_to_action:
            parts.append(self.call_to_action)
        parts.append(hashtag_str)
        return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# LangChain setup (LCEL)
# ---------------------------------------------------------------------------
llm = ChatOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
    model=MODEL_NAME,
    temperature=0.7,
)

_PROMPT_TEMPLATE = """
You are a professional LinkedIn content creator and social media strategist.
Create an engaging LinkedIn post based on the details below.

Topic:    {topic}
Language: {language}
Tone:     {tone}

Requirements:
1. Write 2–4 concise, engaging paragraphs for the content.
2. Craft a compelling title/headline.
3. Add 3–5 relevant hashtags (no # symbol, comma-separated).
4. Write a specific call-to-action that encourages comments or shares.
5. Write everything in {language} using a {tone} tone.
6. Start with a hook to grab attention immediately.

Respond using EXACTLY this format (no extra text before or after):
TITLE: <your headline>
CONTENT: <your 2-4 paragraph body>
HASHTAGS: <tag1, tag2, tag3>
CALL_TO_ACTION: <your call to action>
"""

prompt = PromptTemplate(
    input_variables=["topic", "language", "tone"],
    template=_PROMPT_TEMPLATE,
)

_post_chain = (
    RunnablePassthrough.assign(
        topic=lambda x: x["topic"],
        language=lambda x: x["language"],
        tone=lambda x: x["tone"],
    )
    | prompt
    | llm
    | StrOutputParser()
)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------
class LinkedInPostAgent:
    """AI agent that generates structured LinkedIn posts using LangChain."""

    async def generate_post(
        self,
        topic: str,
        language: str = "English",
        tone: str = "Professional",
    ) -> LinkedInPost:
        """
        Generate a LinkedIn post.

        Args:
            topic:    Subject of the post (e.g. "AI in Healthcare").
            language: Output language (e.g. "English", "German").
            tone:     Writing tone (e.g. "Professional", "Inspirational").

        Returns:
            A structured LinkedInPost object.
        """
        try:
            raw_text: str = await _post_chain.ainvoke(
                {"topic": topic, "language": language, "tone": tone}
            )
            return self._parse(raw_text, topic)
        except Exception as e:
            print(f"⚠️  Generation error: {e}")
            return self._fallback(topic)

    def _parse(self, text: str, topic: str) -> LinkedInPost:
        """Parse LLM output into a LinkedInPost."""
        lines = text.strip().splitlines()
        title = ""
        hashtags: List[str] = []
        call_to_action = ""
        content_lines: List[str] = []
        parsing_content = False

        for line in lines:
            stripped = line.strip()
            upper = stripped.upper()

            if upper.startswith("TITLE:"):
                title = stripped[len("TITLE:"):].strip()
                parsing_content = False
            elif upper.startswith("CONTENT:"):
                parsing_content = True
                body = stripped[len("CONTENT:"):].strip()
                if body:
                    content_lines.append(body)
            elif upper.startswith("HASHTAGS:"):
                tag_str = stripped[len("HASHTAGS:"):].strip()
                hashtags = [t.strip().lstrip("#") for t in tag_str.split(",") if t.strip()]
                parsing_content = False
            elif upper.startswith("CALL_TO_ACTION:"):
                call_to_action = stripped[len("CALL_TO_ACTION:"):].strip()
                parsing_content = False
            elif parsing_content and stripped:
                content_lines.append(stripped)

        return LinkedInPost(
            title=title or f"Professional Insights on {topic}",
            content="\n\n".join(content_lines) or f"Here are my thoughts on {topic}.",
            hashtags=hashtags or ["professional", "insights", "networking"],
            call_to_action=call_to_action or "What are your thoughts? Let's discuss below!",
        )

    def _fallback(self, topic: str) -> LinkedInPost:
        """Return a safe fallback post when generation fails."""
        return LinkedInPost(
            title=f"Professional Insights on {topic}",
            content=(
                f"As professionals, we are constantly navigating the evolving landscape of {topic}. "
                "This topic presents both challenges and opportunities that deserve our attention. "
                "I'd love to hear your perspectives."
            ),
            hashtags=["professional", "insights", "networking", "industry"],
            call_to_action="What's your take? Let's discuss in the comments below!",
        )


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
async def main() -> None:
    agent = LinkedInPostAgent()

    demo_requests = [
        {"topic": "AI in Healthcare", "language": "English", "tone": "Professional"},
        {"topic": "Remote Work Productivity", "language": "English", "tone": "Inspirational"},
    ]

    print("🚀 LinkedIn Post Generator — CLI Demo")
    print("=" * 55)

    for i, req in enumerate(demo_requests, 1):
        print(f"\n📝 Demo {i}: '{req['topic']}' | {req['language']} | {req['tone']}")
        print("-" * 45)
        post = await agent.generate_post(**req)
        print(post.format_post())
        print("=" * 55)

    # Interactive loop
    print("\n🎯 Interactive Mode  (type 'quit' to exit)")
    print("Format: Topic, Language, Tone   e.g. → Machine Learning, English, Casual\n")

    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in ("quit", "exit", "q"):
                print("👋 Goodbye!")
                break
            if not user_input:
                continue

            parts = [p.strip() for p in user_input.split(",")]
            topic = parts[0]
            language = parts[1] if len(parts) > 1 else "English"
            tone = parts[2] if len(parts) > 2 else "Professional"

            print(f"\n🔄 Generating post about '{topic}' in {language} ({tone} tone)…\n")
            post = await agent.generate_post(topic, language, tone)
            print(post.format_post())
            print("=" * 55)

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
