import json


with open("image_info_test-dev2017.json", "r", encoding="utf-8") as f:
    data = json.load(f)


num_images = len(data["images"])
print("Кількість фотографій:", num_images)


num_categories = len(data["categories"])
print("Кількість категорій:", num_categories)


img_info = None
for img in data["images"]:
    if img["file_name"] == "000000000001.jpg":
        img_info = img
        break

if img_info:
    print("\nІнформація про 000000000001.jpg:")
    print("URL:", img_info["coco_url"])
    print("Height:", img_info["height"])
    print("Width:", img_info["width"])
    print("ID:", img_info["id"])


max_image = max(data["images"], key=lambda x: x["file_name"])

print("\nФото з найбільшим номером:")
print(max_image["file_name"])