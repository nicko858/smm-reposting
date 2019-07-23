from telegram.error import NetworkError

from dotenv import load_dotenv
from os import getenv
from external_api import (
    upload_photo_to_vk,
    save_img_to_vk,
    get_vk_upload_adress,
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


def open_img_to_upload(path_to_img):
    img_object = open(path_to_img, 'rb')
    img_obj_for_vk = {'photo': img_object}
    return img_obj_for_vk, img_object


if __name__ == '__main__':
    load_dotenv()
    args = get_args()
    img_file_path = args.path_to_img_file
    message = args.message
    vk_access_token = getenv("vk_access_token")
    vk_group_id = getenv("vk_group_id")
    bot_token = getenv("telegram_bot_token")
    chat_id = getenv("telegram_channel_name")
    facebook_access_token = getenv("facebook_token")
    facebook_group_id = getenv("facebook_group")
    img_obj_for_vk, img_obj = open_img_to_upload(img_file_path)
    try:
        upload_url = get_vk_upload_adress(
            vk_group_id,
            vk_access_token
        )
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
        post_to_facebook(
            facebook_access_token,
            facebook_group_id,
            img_obj,
            message
        )
    except FaceBookAPIUnavailable as error:
        print("Error during Facebook posting:\n{}".format(error))
    try:
        post_to_telegram(
            img_obj,
            message,
            chat_id,
            bot_token
        )
    except NetworkError as error:
        print("Error during Telegram posting:\n{}".format(error))
    finally:
        img_obj.close()
