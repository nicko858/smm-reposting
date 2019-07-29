from telegram.error import NetworkError

from dotenv import load_dotenv
from os import getenv
from external_api import (
    upload_photo_to_vk,
    save_img_to_vk,
    get_vk_upload_address,
    post_photo_to_vk_wall
)
from external_api import post_to_facebook, post_to_telegram
from external_api import FaceBookAPIUnavailable, VkAPIUnavailable
import argparse
from argparse import ArgumentTypeError
from os import access, path, W_OK


def check_file_path(file_path):
    if not access(path.dirname(file_path), W_OK):
        raise ArgumentTypeError(
            "You don't have permissions to '{}' , "
            "or directory doesn't exist!".format(file_path)
        )
    elif path.isdir(file_path):
        raise ArgumentTypeError(
            "The '{}' is not a file!".format(file_path)
        )
    else:
        return file_path


def get_args():
    script_usage = "python reposting.py  <path_to_img_file> <message>"
    parser = argparse.ArgumentParser(
        description="How to run reposting.py:",
        usage=script_usage
    )
    parser.add_argument(
        "path_to_img_file",
        type=check_file_path,
        help="Specify the path img_file"
    )
    parser.add_argument(
        "message",
        type=str,
        help="Specify the post message"
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    load_dotenv()
    args = get_args()
    img_file_path = args.path_to_img_file
    message = args.message

    vk_access_token = getenv("VK_ACCESS_TOKEN")
    vk_group_id = getenv("VK_GROUP_ID")
    bot_token = getenv("TELEGRAM_BOT_TOKEN")
    chat_id = getenv("TELEGRAM_CHANNEL_NAME")
    facebook_access_token = getenv("FACEBOOK_TOKEN")
    facebook_group_id = getenv("FACEBOOK_GROUP")

    try:
        upload_url = get_vk_upload_address(
            vk_group_id,
            vk_access_token
        )
        with open(img_file_path, 'rb') as img_file:
            img_obj_for_vk = {'photo': img_file}
            uploaded_photo, server, img_hash = upload_photo_to_vk(
                upload_url,
                img_obj_for_vk
            )
        media_id, owner_id = save_img_to_vk(
            vk_access_token,
            uploaded_photo,
            vk_group_id,
            server,
            img_hash
        )
        post_photo_to_vk_wall(
            vk_group_id,
            owner_id,
            media_id,
            message,
            vk_access_token
        )
    except VkAPIUnavailable as error:
        print("Error during VK posting:\n{}".format(error))

    try:
        with open(img_file_path, 'rb') as img_file:
            post_to_facebook(
                facebook_access_token,
                facebook_group_id,
                img_file,
                message
            )
    except FaceBookAPIUnavailable as error:
        print("Error during Facebook posting:\n{}".format(error))

    try:
        with open(img_file_path, 'rb') as img_file:
            post_to_telegram(
                img_file,
                message,
                chat_id,
                bot_token
            )
    except NetworkError as error:
        print("Error during Telegram posting:\n{}".format(error))

