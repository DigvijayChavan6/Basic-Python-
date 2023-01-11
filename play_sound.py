from playsound import playsound
import  time as t
cnt=0
while True:
    playsound('/home/digvijay/Music/DAKU_(SLOWED_AND_REVERBED_)_INDERPAL_MOGA_|_LOFI_CURE(256k).mp3')
    cnt+=1;
    if cnt==5:
        break
    t.sleep(2)