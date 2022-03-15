
import json
import firebase_admin
from firebase_admin import credentials,messaging

# cred = credentials.Certificate('./firebasekey.json')
cred = credentials.Certificate('androidapi/crtd-main-firebase-adminsdk-hwta9-3a25d9097e.json')
app=firebase_admin.initialize_app(cred)

def sendpushnotification(applytype,mssg,token,empid):
    try:
      if token!=None and len(token)>0:
        data={
            
        "applytype":applytype,
        "mssg":mssg,
        "empid":str(empid)

        
        }
        message =  messaging.Message(
            
            
            token=token,
            # token="dsdMny-QRo6r1ABKxjTc56:APA91bHQzJGoEMbSwB5VZcDDWl88DGWT8CfPTxh3SUq6nSXY_z7Y9VB5cHtdtfk22EMZZythMvhCVwMK_HfF8HGn9nL9noDnxWPrcm8Fo62b0sAy-1ssGdS8BjQ3l9CgIo0Z6Y5DcWLz",
            data=data
        
        
        )

        # Send a message to the devices subscribed to the provided topic.
        response = messaging.send(message)
    except Exception as e:
        pass
