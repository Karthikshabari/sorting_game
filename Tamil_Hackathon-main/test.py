import random

dict ={"விலங்குகள்":["ஒட்டகம்","கரடி","குதிரை","சிங்கம்","நரி","நாய்","பசு","மான்","யானை"],
      "கிரகங்கள்":["சனி,செவ்வாய்,நெப்டியூன்,புதன்,பூமி,யுரேனஸ்,வியாழன்,வெள்ளி"],
      "காய்கறிகள்":["அவரைக்காய்,கத்தரிக்காய்,காரட்,கோவைக்காய்,தக்காளி,புடலங்காய்,பூசணிக்காய்,மாங்காய்,முருங்கைக்காய்"],
      "வண்ணங்கள்":["ஆரஞ்சு,ஊதா,கருப்பு,சிவப்பு,தங்க,நீலம்,மஞ்சள்,பச்சை,வெள்ளி,வெள்ளை"],
      "பழங்கள்":["அன்னாசிப்பழம்,ஆப்பிள்,எலுமிச்சை்ப்பழம்,தர்பூசணி,பசிப்பாழம்,பப்பாளி,பேரிக்காய்,மாதுளம் பழம்,வாழைப்பழம்,வுெண்ணைப்பழம்"],
      "கிழமைகள்":["சனிக்கிழமை,செவ்வாய் கிழமை,ஞாயிற்றுக்கிழமை,திங்கட்கிழமை,வியாழன்,வெள்ளி"],
      "மாதங்கள்":["ஐப்பாசி,ஆடி,ஆணி,ஆவணி,கார்த்திகை,சித்திரை,பங்குனி,புரட்டாசி,மாசி,மார்கழி,வைகாசி"]}

l=dict.get("விலங்குகள்")
print(random.sample(l, 5))

key_list = list(dict.keys())
print(key_list)
print(key_list[4])
for i in key_list:
      if i != "கிழமைகள்":
            daycount = 1
      else:
            daycount = 0
print(daycount)