import qrcode
from github import Github
import os

# GitHub repository details
github_token = 'YOUR_GITHUB_TOKEN'
repository_name = 'YOUR_REPOSITORY_NAME'
repo_owner = 'YOUR_GITHUB_USERNAME'

def generate_qr_code(content, image_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(image_path)

def upload_to_github(token, repo_name, owner, file_path):
    g = Github(token)
    repo = g.get_user(owner).get_repo(repo_name)
    with open(file_path, 'rb') as file:
        content = file.read()
    file_name = os.path.basename(file_path)
    repo.create_file(file_name, f'Adding QR code image', content, branch='main')
    print(f"QR code image '{file_name}' uploaded to '{repo_name}' repository on GitHub.")

if __name__ == "__main__":
    # Content for the QR code (e.g., a URL)
    qr_content = 'https://example.com'

    # Generate QR code
    qr_code_image_path = 'qr_code.png'
    generate_qr_code(qr_content, qr_code_image_path)

    # Upload QR code image to GitHub repository
    upload_to_github(github_token, repository_name, repo_owner, qr_code_image_path)

    # Delete the QR code image after uploading (optional)
    os.remove(qr_code_image_path)
