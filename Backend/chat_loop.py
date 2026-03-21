# import sys
# import json
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-2.5-flash")


# def chat_with_model(data):

#     user_message = data["user_message"].strip().lower()
#     itinerary = data["current_itinerary"]
#     pending_update = data.get("pending_update")

#     # ==================================================
#     # STEP 1: If waiting for confirmation
#     # ==================================================

#     if pending_update:

#         if user_message == "yes":
#             return {
#                 "action": "confirm_update",
#                 "updated_itinerary": pending_update
#             }

#         elif user_message == "no":
#             return {
#                 "action": "cancel_update",
#                 "reply": "👍 No changes were made to your itinerary."
#             }

#         else:
#             return {
#                 "action": "normal_reply",
#                 "reply": "Please reply with YES to confirm changes or NO to cancel."
#             }

#     # ==================================================
#     # STEP 2: Normal Chat or Modification
#     # ==================================================

#     prompt = f"""
# You are an AI travel assistant.

# Current itinerary:
# {itinerary}

# User message:
# {user_message}

# Instructions:

# 1. If user asks general question → answer normally.

# 2. If user wants to modify itinerary:
#    - Don't Explain changes. just start from Trip Overview
#    - Then provide FULL updated itinerary.
#    - At the end write exactly:

#    Reply YES to confirm changes or NO to cancel.

# IMPORTANT:
# Return plain text only.
# Do not use markdown.
# """

#     response = model.generate_content(prompt)
#     reply_text = response.text.strip()

#     # ==================================================
#     # DETECT MODIFICATION
#     # ==================================================

#     if "reply yes to confirm changes" in reply_text.lower():

#         # 🔥 Extract itinerary part BEFORE confirmation line
#         split_text = reply_text.split("Reply YES to confirm changes or NO to cancel.")

#         updated_itinerary_only = split_text[0].strip()

#         return {
#             "action": "pending_update",
#             "reply": reply_text,
#             "updated_itinerary": updated_itinerary_only
#         }

#     else:
#         return {
#             "action": "normal_reply",
#             "reply": reply_text
#         }


# if __name__ == "__main__":
#     try:
#         data = json.loads(sys.argv[1])
#         result = chat_with_model(data)
#         print(json.dumps(result))
#     except Exception as e:
#         print(json.dumps({"error": str(e)}))




# import sys
# import json
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-2.5-flash")


# def chat_with_model(data):

#     user_message = data["user_message"].strip()
#     lower_message = user_message.lower()
#     itinerary = data["current_itinerary"]
#     pending_update = data.get("pending_update")

#     # ==================================================
#     # STEP 1: If waiting for confirmation
#     # ==================================================

#     if pending_update:

#         if lower_message == "yes":
#             return {
#                 "action": "confirm_update",
#                 "updated_itinerary": pending_update
#             }

#         elif lower_message == "no":
#             return {
#                 "action": "cancel_update",
#                 "reply": "👍 No changes were made to your itinerary."
#             }

#         else:
#             return {
#                 "action": "normal_reply",
#                 "reply": "Please reply with YES to confirm changes or NO to cancel."
#             }

#     # ==================================================
#     # STEP 2: Normal Chat or Modification
#     # ==================================================

#     prompt = f"""
# You are an AI travel assistant.

# Current itinerary:
# {itinerary}

# User message:
# {user_message}

# Instructions:

# 1. If user asks general question → answer normally.

# 2. If user wants to modify itinerary:
#    - Don't Explain changes. just start from Trip Overview
#    - Then provide FULL updated itinerary.
#    - At the end write exactly:

#    Reply YES to confirm changes or NO to cancel.

# IMPORTANT:
# Return plain text only.
# Do not use markdown.
# """

#     response = model.generate_content(prompt)
#     reply_text = response.text.strip()

#     # ==================================================
#     # DETECT MODIFICATION
#     # ==================================================

#     if "reply yes to confirm changes" in reply_text.lower():

#         # 🔥 Extract itinerary part BEFORE confirmation line
#         split_text = reply_text.split("Reply YES to confirm changes or NO to cancel.")

#         updated_itinerary_only = split_text[0].strip()

#         return {
#             "action": "pending_update",
#             "reply": reply_text,
#             "updated_itinerary": updated_itinerary_only
#         }

#     else:
#         return {
#             "action": "normal_reply",
#             "reply": reply_text
#         }


# if __name__ == "__main__":
#     try:
#         data = json.loads(sys.argv[1])
#         result = chat_with_model(data)
#         print(json.dumps(result))
#     except Exception as e:
#         print(json.dumps({"error": str(e)}))



# import sys
# import json
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-2.5-flash")


# def chat_with_model(data):

#     user_message = data["user_message"].strip()
#     lower_message = user_message.lower()
#     itinerary = data["current_itinerary"]
#     pending_update = data.get("pending_update")

#     # ================= STEP 1 =================
#     if pending_update:

#         if lower_message == "yes":
#             return {
#                 "action": "confirm_update",
#                 "updated_itinerary": pending_update
#             }

#         elif lower_message == "no":
#             return {
#                 "action": "cancel_update",
#                 "reply": "👍 No changes were made."
#             }

#         else:
#             return {
#                 "action": "normal_reply",
#                 "reply": "Reply YES to confirm or NO to cancel."
#             }

#     # ================= STEP 2 =================

# if "change" in lower_message:
#     return {
#         "action": "pending_update",
#         "reply": "Test update. Reply YES",
#         "updated_itinerary": "🔥 NEW PLAN TEST"
#     }

#     prompt = f"""
# You are an AI travel assistant.

# Current itinerary:
# {itinerary}

# User message:
# {user_message}

# If modification:
# - Return FULL updated itinerary
# - End with:
# Reply YES to confirm changes or NO to cancel.
# """

#     # response = model.generate_content(prompt)
#     # reply_text = response.text.strip()
#     try:
#         response = model.generate_content(prompt)
#         if not response or not response.text:
#             return {
#             "action": "normal_reply",
#             "reply": "⚠️ AI not responding. Try again."
#            }
#         reply_text = response.text.strip()
#     except Exception as e: 
#         print("Gemini API error:", str(e))
#         return {
#           "action": "normal_reply",
#         "reply": "⚠️ AI service error. Try again later."
#         }

#     if "reply yes to confirm changes" in reply_text.lower():

#         updated_itinerary = reply_text.split(
#             "Reply YES to confirm changes or NO to cancel."
#         )[0].strip()

#         return {
#             "action": "pending_update",
#             "reply": reply_text,
#             "updated_itinerary": updated_itinerary
#         }

#     return {
#         "action": "normal_reply",
#         "reply": reply_text
#     }


# if __name__ == "__main__":
#     try:
#         data = json.loads(sys.argv[1])
#         result = chat_with_model(data)
#         print(json.dumps(result))
#     except Exception as e:
#         print(json.dumps({"error": str(e)}))
   
#     # data = json.loads(sys.argv[1])
#     # result = chat_with_model(data)
#     # print(json.dumps(result))


# import sys
# import json
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-2.5-flash")

# print("🔥 FUNCTION CALLED")
# print("USER MESSAGE:", user_message)
# def chat_with_model(data):

#     user_message = data["user_message"].strip()
#     lower_message = user_message.lower()
#     itinerary = data["current_itinerary"]
#     pending_update = data.get("pending_update")

#     # ================= STEP 1 =================
#     if pending_update:

#         if lower_message == "yes":
#             return {
#                 "action": "confirm_update",
#                 "updated_itinerary": pending_update
#             }

#         elif lower_message == "no":
#             return {
#                 "action": "cancel_update",
#                 "reply": "👍 No changes were made."
#             }

#         else:
#             return {
#                 "action": "normal_reply",
#                 "reply": "Reply YES to confirm or NO to cancel."
#             }

#     # ================= STEP 2 (TEST BLOCK) =================
#     # if "change" in lower_message:
#     #     return {
#     #         "action": "pending_update",
#     #         "reply": "Test update. Reply YES",
#     #         "updated_itinerary": "🔥 NEW PLAN TEST"
#     #     }
#     # ================= STEP 2 (FORCE TEST) =================
# print("🔥 CHECKING CHANGE BLOCK")

# if "change" in lower_message:
#     print("✅ CHANGE DETECTED")
#     return {
#         "action": "pending_update",
#         "reply": "Test update working. Reply YES",
#         "updated_itinerary": "🔥 NEW PLAN UPDATED SUCCESSFULLY"
#     }

#     # ================= STEP 3 =================
#     prompt = f"""
# You are an AI travel assistant.

# Current itinerary:
# {itinerary}

# User message:
# {user_message}

# If modification:
# - Return FULL updated itinerary
# - End with:
# Reply YES to confirm changes or NO to cancel.
# """

#     try:
#         response = model.generate_content(prompt)

#         if not response or not response.text:
#             return {
#                 "action": "normal_reply",
#                 "reply": "⚠️ AI not responding. Try again."
#             }

#         reply_text = response.text.strip()

#     except Exception as e:
#         print("Gemini API error:", str(e))
#         return {
#             "action": "normal_reply",
#             "reply": "⚠️ AI service error. Try again later."
#         }

#     if "reply yes to confirm changes" in reply_text.lower():

#         updated_itinerary = reply_text.split(
#             "Reply YES to confirm changes or NO to cancel."
#         )[0].strip()

#         return {
#             "action": "pending_update",
#             "reply": reply_text,
#             "updated_itinerary": updated_itinerary
#         }

#     return {
#         "action": "normal_reply",
#         "reply": reply_text
#     }


# if __name__ == "__main__":
#     try:
#         data = json.loads(sys.argv[1])
#         result = chat_with_model(data)
#         print(json.dumps(result))
#     except Exception as e:
#         print(json.dumps({"error": str(e)}))

import sys
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


def chat_with_model(data):

    user_message = data["user_message"].strip()
    lower_message = user_message.lower()
    itinerary = data["current_itinerary"]
    pending_update = data.get("pending_update")

    print("🔥 FUNCTION CALLED")
    print("USER MESSAGE:", user_message)

    # ================= STEP 1 =================
    if pending_update:

        if lower_message == "yes":
            return {
                "action": "confirm_update",
                "updated_itinerary": pending_update
            }

        elif lower_message == "no":
            return {
                "action": "cancel_update",
                "reply": "👍 No changes were made."
            }

        else:
            return {
                "action": "normal_reply",
                "reply": "Reply YES to confirm or NO to cancel."
            }

    # ================= STEP 2 (TEST BLOCK) =================
    print("🔥 CHECKING CHANGE BLOCK")

    if "change" in lower_message:
        print("✅ CHANGE DETECTED")

        return {
            "action": "pending_update",
            "reply": "Test update working. Reply YES",
            "updated_itinerary": "🔥 NEW PLAN UPDATED SUCCESSFULLY"
        }

    # ================= STEP 3 =================
    prompt = f"""
You are an AI travel assistant.

Current itinerary:
{itinerary}

User message:
{user_message}

If modification:
- Return FULL updated itinerary
- End with:
Reply YES to confirm changes or NO to cancel.
"""

    try:
        response = model.generate_content(prompt)

        if not response or not response.text:
            return {
                "action": "normal_reply",
                "reply": "⚠️ AI not responding. Try again."
            }

        reply_text = response.text.strip()

    except Exception as e:
        print("Gemini API error:", str(e))
        return {
            "action": "normal_reply",
            "reply": "⚠️ AI service error. Try again later."
        }

    if "reply yes to confirm changes" in reply_text.lower():

        updated_itinerary = reply_text.split(
            "Reply YES to confirm changes or NO to cancel."
        )[0].strip()

        return {
            "action": "pending_update",
            "reply": reply_text,
            "updated_itinerary": updated_itinerary
        }

    return {
        "action": "normal_reply",
        "reply": reply_text
    }


if __name__ == "__main__":
    try:
        data = json.loads(sys.argv[1])
        result = chat_with_model(data)
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"error": str(e)}))