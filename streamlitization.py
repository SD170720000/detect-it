import configparser
import tweepy
import streamlit as st
import tensorflow as tf

#------configuration------#
config = configparser.ConfigParser()
config.read('config.ini')
get = config['twitter']

#------tokenization------#
api_key = get['api_key']
api_key_secret = get['api_key_secret']
access_token = get['access_token']
access_token_secret = get['access_token_secret']

#------authentication------#
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#------streamlitiztion------#
st.title('Fake Profile Detection')


screenName = st.text_input('Enter twitter User Name','')

try:
    if screenName == '':
        st.warning('Enter a Valid User Name')
    else:
        user = api.get_user(screen_name='@'+screenName)

        data = {
            'user_id': user.id,
            'user_name': user.name,
            'user_screen_name': user.screen_name,
            'user_total_statuses_count': user.statuses_count,
            'user_total_followers_count': user.followers_count,
            'user_total_friends_count': user.friends_count,
            'user_total_favorites_count':user.favourites_count,
            'user_total_listed_count':user.listed_count,
            'user_data' : [user.statuses_count,user.followers_count,user.friends_count,user.favourites_count,user.listed_count]
        }

        st.write(f"UserName: {data['user_name']}")
        st.write(f"User ScreenName: {data['user_screen_name']}")
        st.write(f"Statuses Count: {data['user_total_statuses_count']}")
        st.write(f"Followers Count: {data['user_total_followers_count']}")
        st.write(f"Friends Count: {data['user_total_friends_count']}")
        st.write(f"Favorites Count: {data['user_total_favorites_count']}")
        st.write(f"Listed Count: {data['user_total_listed_count']}")
        classifier_model = tf.keras.models.load_model('model_h5')
        preds = classifier_model.predict(tf.expand_dims(data['user_data'],axis=0))
        if tf.round(tf.squeeze(preds)):
            st.write(f"Prediction Value: Real Profile")
        else:
            st.write(f"Prediction Value: Fake Profile")
        st.write(f'Prediction Value: {tf.round(tf.squeeze(preds))}')
except:
    st.error('Invalid User! Please enter a valid User Name')
