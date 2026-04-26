"""
test_agent.py
-------------
Quick test script for the LinkedIn Post Agent.
Run from the project root: python App/test_agent.py
"""

import asyncio
import os
from dotenv import load_dotenv

load_dotenv()


async def test_linkedin_agent() -> None:
    if not os.getenv("API_KEY"):
        print("❌ API_KEY not found. Add it to your .env file and try again.")
        return

    try:
        from App.linkedin_post_agent import LinkedInPostAgent
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Run: pip install -r requirements.txt")
        return

    print("🚀 LinkedIn Post Agent — Test Suite")
    print("=" * 50)

    agent = LinkedInPostAgent()

    test_cases = [
        {"topic": "Machine Learning in Finance", "language": "English", "tone": "Professional"},
        {"topic": "Sustainable Technology",      "language": "Spanish",  "tone": "Inspirational"},
        {"topic": "Digital Transformation",      "language": "German",   "tone": "Casual"},
    ]

    passed = 0
    for i, case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {case['topic']} | {case['language']} | {case['tone']}")
        print("-" * 45)
        try:
            post = await agent.generate_post(**case)

            # Basic assertions
            assert post.title, "Title should not be empty"
            assert post.content, "Content should not be empty"
            assert len(post.hashtags) >= 1, "Should have at least one hashtag"
            assert post.call_to_action, "CTA should not be empty"

            print("✅ PASSED")
            print(post.format_post())
            print("=" * 50)
            passed += 1

        except AssertionError as e:
            print(f"❌ ASSERTION FAILED: {e}")
        except Exception as e:
            print(f"❌ ERROR: {e}")

    print(f"\n🎯 Results: {passed}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    asyncio.run(test_linkedin_agent())
