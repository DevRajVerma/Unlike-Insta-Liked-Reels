from instagrapi import Client
import time
import random
import uuid
from datetime import datetime
import logging

def generate_uuid():
    """Generate a random UUID"""
    return str(uuid.uuid4())

def safe_unlike_posts(username, password, max_unlikes_per_hour=50, max_unlikes_per_day=200):
    """
    Safely unlike Instagram posts with rate limiting and clean output
    """
    # Set up logging with simplified format
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',  # Only show the message, no timestamp or level
        handlers=[
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    
    cl = Client()
    
    # Set up custom settings
    DEVICE_SETTINGS = {
        "app_version": "269.0.0.18.75",
        "android_version": 26,
        "android_release": "8.0.0",
        "dpi": "480dpi",
        "resolution": "1080x1920",
        "manufacturer": "OnePlus",
        "device": "GT-I9500",
        "model": "SM-G973F",
        "cpu": "universal7880",
        "version_code": "314665256"
    }

    session_settings = {
        "user_agent": "Instagram 269.0.0.18.75 Android (26/8.0.0; 480dpi; 1080x1920; OnePlus; GT-I9500; SM-G973F; universal7880; en_US; 314665256)",
        "device_settings": DEVICE_SETTINGS,
        "uuids": {
            "phone_id": generate_uuid(),
            "uuid": generate_uuid(),
            "client_session_id": generate_uuid(),
            "advertising_id": generate_uuid(),
            "android_device_id": generate_uuid(),
        }
    }

    cl.set_settings(session_settings)
    cl.set_user_agent()

    logger.info("🔄 Logging in to Instagram...")
    try:
        cl.login(username, password)
        logger.info("✅ Login successful!")
        
        liked_posts = []
        
        # Try different methods to find liked posts
        logger.info("🔍 Searching for your liked posts...")
        
        # Method 1: Direct liked posts
        try:
            liked_media = cl.liked_medias()
            liked_posts.extend(liked_media)
        except Exception:
            pass
            
        # Method 2: User's feed
        try:
            user_id = cl.user_id_from_username(username)
            user_feed = cl.user_medias_v1(user_id, amount=50)
            for media in user_feed:
                try:
                    media_info = cl.media_info(media.pk)
                    if hasattr(media_info, 'has_liked') and media_info.has_liked:
                        liked_posts.append(media)
                except Exception:
                    continue
        except Exception:
            pass

        if not liked_posts:
            logger.info("❌ No liked posts found!")
            return

        logger.info(f"📝 Found {len(liked_posts)} liked posts")
        
        # Initialize counters
        unlikes_this_hour = 0
        unlikes_today = 0
        hour_start = datetime.now()
        day_start = datetime.now()

        # Unlike posts
        for i, media in enumerate(liked_posts, 1):
            try:
                current_time = datetime.now()
                
                # Check limits
                if (current_time - day_start).total_seconds() >= 86400:
                    unlikes_today = 0
                    day_start = current_time
                
                if (current_time - hour_start).total_seconds() >= 3600:
                    unlikes_this_hour = 0
                    hour_start = current_time
                
                if unlikes_today >= max_unlikes_per_day:
                    logger.info("⏳ Daily limit reached. Waiting for next day...")
                    time.sleep(3600)
                    continue
                    
                if unlikes_this_hour >= max_unlikes_per_hour:
                    wait_time = 3600 - (current_time - hour_start).total_seconds()
                    logger.info(f"⏳ Hourly limit reached. Waiting {wait_time/60:.1f} minutes...")
                    time.sleep(wait_time)
                    continue

                media_id = media.pk if hasattr(media, 'pk') else getattr(media, 'id', None)
                
                if media_id:
                    success = cl.media_unlike(media_id)
                    if success:
                        unlikes_this_hour += 1
                        unlikes_today += 1
                        logger.info(f"✅ Unliked post {i}/{len(liked_posts)} | This hour: {unlikes_this_hour}/{max_unlikes_per_hour} | Today: {unlikes_today}/{max_unlikes_per_day}")
                    else:
                        logger.info(f"❌ Failed to unlike post {i}/{len(liked_posts)}")
                
                # Random delay
                time.sleep(random.uniform(5, 10))

            except Exception as e:
                logger.info(f"⚠️ Error while unliking post {i}: {str(e)}")
                time.sleep(60)
                continue

        logger.info("✨ Completed unliking process!")
        
    except Exception as e:
        logger.info(f"❌ An error occurred: {str(e)}")
    finally:
        cl.logout()
        logger.info("👋 Logged out of Instagram")

if __name__ == "__main__":
    username = "your_username" #enter your instagram username here
    password = "your_password" #enter your instagram password here
    safe_unlike_posts(username, password)