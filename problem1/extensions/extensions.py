answer = input("File name: ")

answer = answer.strip().lower()

if answer.endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
    extension = answer.rsplit(".")[-1]

    match extension:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
else:
    print("application/octet-stream")

