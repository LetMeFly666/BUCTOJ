'''
Author: LetMeFly
Date: 2022-02-23 15:24:31
LastEditors: LetMeFly
LastEditTime: 2022-02-23 15:51:32
'''
from setup import version
import requests
import json
import os

headers = {
    "Content-Type": "application/bat",
    "Authorization": f"token {os.environ.get('REPO_TOKEN')}",
}
tag_name = f"v{version}"


def create1release() -> int:
    """
    创建名为{tag_name}的release并且返回releaseId
    """
    url = "https://api.github.com/repos/LetMeFly666/BUCTOJ/releases"
    data = json.dumps({
        "tag_name": tag_name,
        "name": tag_name,
        "body": tag_name,
        "generate_release_notes": True
    })
    response = requests.post(url, headers=headers, data=data)
    print(response)
    return response.json().get("id")


def upload_files2release(release_id: str) -> None:
    """上传文件到release"""
    for this_file in os.listdir("dist"):
        params = (
            ('name', this_file),
            ('label', this_file),
        )
        data = open(os.path.join("dist", this_file), 'rb').read()
        response = requests.post(f'https://uploads.github.com/repos/LetMeFly666/BUCTOJ/releases/{release_id}/assets', headers=headers, params=params, data=data)
        print(response)



def main():
    release_id = create1release()
    upload_files2release(str(release_id))


if __name__ == "__main__":
    main()
