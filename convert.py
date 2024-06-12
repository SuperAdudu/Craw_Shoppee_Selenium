# import pickle
# cookie_text = "__LOCALE__null=VN; _gcl_au=1.1.246320093.1712132234; csrftoken=O9DVtyRUVTLVLcD3O5dCJQX5MbhtZXih; SPC_F=8S62yu34SDZSgBOOi5qF6OUZg3MPe1jK; REC_T_ID=94000840-f192-11ee-a9e2-46a568a38541; SPC_SI=KYACZgAAAABSbDZtd2oxYcpmvgAAAAAAUU5DR2dQZG4=; SPC_SEC_SI=v1-SlE1N1hWa29FNGhqVzJKWGDFlhyTw0ibBLX2Rt/5sIU93M/ULVsNYnWd+vJVvyJ7EiX/VJbCnI5bImfGfDmPlRS5VdTag+goT9AXzQsA1ng=; _sapid=fff317fc75e31a9a747a7dbf6af2fc8274a85f8341a296c5fdf8a70b; _QPWSDCXHZQA=b8966b5d-d2ed-41a8-9671-c43e2f20040c; REC7iLP4Q=3f95a52c-9da2-4c86-bbb4-c0064ff89343; SPC_IA=1; _gid=GA1.2.1056547633.1712132236; SPC_CLIENTID=OFM2Mnl1MzRTRFpTudjzwhgpfyehalls; SPC_U=116367905; SPC_R_T_ID=HkR3jHB1sfUYQfjdDjfCv6Sk1okQmvOHqWb8MtcbV8LecHzvs0JojpXK7N6GtN1ODJgtwQvFp219MoNqeOeTts/ChNg9I+v1IfAc0K/WGjxZmsFywuL82bYjh8pxuV3EME/wEaj9J0qy8TzdUrvzciy5twBC0X07SFeHucmbBo8=; SPC_R_T_IV=RFBNSjRnOHd5VEFzZDJFUw==; SPC_T_ID=HkR3jHB1sfUYQfjdDjfCv6Sk1okQmvOHqWb8MtcbV8LecHzvs0JojpXK7N6GtN1ODJgtwQvFp219MoNqeOeTts/ChNg9I+v1IfAc0K/WGjxZmsFywuL82bYjh8pxuV3EME/wEaj9J0qy8TzdUrvzciy5twBC0X07SFeHucmbBo8=; SPC_T_IV=RFBNSjRnOHd5VEFzZDJFUw==; _hjSessionUser_868286=eyJpZCI6ImZlMzJhMmY4LTM3ZWQtNTY0NS1iODU1LWNhZWUzNzY1OWU1YyIsImNyZWF0ZWQiOjE3MTIxMzIyMzU2OTQsImV4aXN0aW5nIjp0cnVlfQ==; SPC_EC=.ZEVIbzV0OUdRNlpNTDFMblrpdiIdXq7s4EV1SPv8b7f52K7zE1KF35VRGDRCWsxwd1fVgWDzY9rl0FBTJGjjOg9cIvm4USRRsRf/QqRkQdzoX0ZZcVetLURzOlmc58iwUVw5ZJOIkmXJtCagSfBE1wW1YnAE0VViv0dml99UCaxQ81xAgQlHV/vzmjg8kBXbGgFOHQx3GpNKldhZvkYIdw==; SPC_ST=.ZEVIbzV0OUdRNlpNTDFMblrpdiIdXq7s4EV1SPv8b7f52K7zE1KF35VRGDRCWsxwd1fVgWDzY9rl0FBTJGjjOg9cIvm4USRRsRf/QqRkQdzoX0ZZcVetLURzOlmc58iwUVw5ZJOIkmXJtCagSfBE1wW1YnAE0VViv0dml99UCaxQ81xAgQlHV/vzmjg8kBXbGgFOHQx3GpNKldhZvkYIdw==; shopee_webUnique_ccd=K8YOsYuarcnwAdW7X1mVHQ%3D%3D%7CW9EIObd0bpL7QXQswM%2FoNr2Aiifl9KI7kxWhLtawNBB9Z0Hk09hwlCeb62ca15eDv6AM1xCPPRnjng%3D%3D%7Cdex%2F4nlUAm%2Bpd8Yu%7C08%7C3; ds=10d9fdde79002ff4b39959e76ed68a12; _ga_4GPP1ZXG63=GS1.1.1712139721.3.1.1712140724.32.0.0; _ga=GA1.1.1005638949.1712132235"

# # Tách cookie thành từ điển
# cookie_dict = {}
# for part in cookie_text.split('; '):
#     key, value = part.split('=', 1)
#     cookie_dict[key] = value

# # Lưu cookie vào file .pkl
# with open('cookies.pkl', 'wb') as f:
#     pickle.dump(cookie_dict, f)
from time import sleep
# import requests
link = 'https://shopee.vn/'

# Gửi yêu cầu HTTP để tải nội dung của trang web
# response = requests.get(link)
# sleep(20)

import webbrowser

url = 'https://www.example.com'
webbrowser.open(link)
sleep(60)

