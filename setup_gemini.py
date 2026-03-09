from google import genai
API_KEY = "AIzaSyAZCTRDxww0HB3oCH1NLNByxIOqvoBN804"
client = genai.Client(api_key=API_KEY)

print("Gemini API key đã config thành công với SDK mới!")
print("Client sẵn sàng sử dụng:", client)
print("Bạn có thể dùng client.models.list() hoặc client.models.generate_content() để test.")

