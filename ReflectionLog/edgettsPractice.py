#basically this is the ai voice module which is everywhere in the internet

import asyncio
import edge_tts

async def main():
    edge = edge_tts.Communicate("you motherfucking bitch. i will kill you","en-US-GuyNeural")
    await edge.save("test.mp3")

asyncio.run(main())

#has many many voices 
'''python -m edge_tts --list-voices
ALL VOICES
---------------------------------  --------  ---------------------  --------------------------------------
af-ZA-AdriNeural                   Female    General                Friendly, Positive
af-ZA-WillemNeural                 Male      General                Friendly, Positive
am-ET-AmehaNeural                  Male      General                Friendly, Positive
am-ET-MekdesNeural                 Female    General                Friendly, Positive
ar-AE-FatimaNeural                 Female    General                Friendly, Positive
ar-AE-HamdanNeural                 Male      General                Friendly, Positive
ar-BH-AliNeural                    Male      General                Friendly, Positive
ar-BH-LailaNeural                  Female    General                Friendly, Positive
ar-DZ-AminaNeural                  Female    General                Friendly, Positive
ar-DZ-IsmaelNeural                 Male      General                Friendly, Positive
ar-EG-SalmaNeural                  Female    General                Friendly, Positive
ar-EG-ShakirNeural                 Male      General                Friendly, Positive
ar-IQ-BasselNeural                 Male      General                Friendly, Positive
ar-IQ-RanaNeural                   Female    General                Friendly, Positive
ar-JO-SanaNeural                   Female    General                Friendly, Positive
ar-JO-TaimNeural                   Male      General                Friendly, Positive
ar-KW-FahedNeural                  Male      General                Friendly, Positive
ar-KW-NouraNeural                  Female    General                Friendly, Positive
ar-LB-LaylaNeural                  Female    General                Friendly, Positive
ar-LB-RamiNeural                   Male      General                Friendly, Positive
ar-LY-ImanNeural                   Female    General                Friendly, Positive
ar-LY-OmarNeural                   Male      General                Friendly, Positive
ar-MA-JamalNeural                  Male      General                Friendly, Positive
ar-MA-MounaNeural                  Female    General                Friendly, Positive
ar-OM-AbdullahNeural               Male      General                Friendly, Positive
ar-OM-AyshaNeural                  Female    General                Friendly, Positive
ar-QA-AmalNeural                   Female    General                Friendly, Positive
ar-QA-MoazNeural                   Male      General                Friendly, Positive
ar-SA-HamedNeural                  Male      General                Friendly, Positive
ar-SA-ZariyahNeural                Female    General                Friendly, Positive
ar-SY-AmanyNeural                  Female    General                Friendly, Positive
ar-SY-LaithNeural                  Male      General                Friendly, Positive
ar-TN-HediNeural                   Male      General                Friendly, Positive
ar-TN-ReemNeural                   Female    General                Friendly, Positive
ar-YE-MaryamNeural                 Female    General                Friendly, Positive
ar-YE-SalehNeural                  Male      General                Friendly, Positive
az-AZ-BabekNeural                  Male      General                Friendly, Positive
az-AZ-BanuNeural                   Female    General                Friendly, Positive
bg-BG-BorislavNeural               Male      General                Friendly, Positive
bg-BG-KalinaNeural                 Female    General                Friendly, Positive
bn-BD-NabanitaNeural               Female    General                Friendly, Positive
bn-BD-PradeepNeural                Male      General                Friendly, Positive
bn-IN-BashkarNeural                Male      General                Friendly, Positive
bn-IN-TanishaaNeural               Female    General                Friendly, Positive
bs-BA-GoranNeural                  Male      General                Friendly, Positive
bs-BA-VesnaNeural                  Female    General                Friendly, Positive
ca-ES-EnricNeural                  Male      General                Friendly, Positive
ca-ES-JoanaNeural                  Female    General                Friendly, Positive
cs-CZ-AntoninNeural                Male      General                Friendly, Positive
cs-CZ-VlastaNeural                 Female    General                Friendly, Positive
cy-GB-AledNeural                   Male      General                Friendly, Positive
cy-GB-NiaNeural                    Female    General                Friendly, Positive
da-DK-ChristelNeural               Female    General                Friendly, Positive
da-DK-JeppeNeural                  Male      General                Friendly, Positive
de-AT-IngridNeural                 Female    General                Friendly, Positive
de-AT-JonasNeural                  Male      General                Friendly, Positive
de-CH-JanNeural                    Male      General                Friendly, Positive
de-CH-LeniNeural                   Female    General                Friendly, Positive
de-DE-AmalaNeural                  Female    General                Friendly, Positive
de-DE-ConradNeural                 Male      General                Friendly, Positive
de-DE-FlorianMultilingualNeural    Male      General                Friendly, Positive
de-DE-KatjaNeural                  Female    General                Friendly, Positive
de-DE-KillianNeural                Male      General                Friendly, Positive
de-DE-SeraphinaMultilingualNeural  Female    General                Friendly, Positive
el-GR-AthinaNeural                 Female    General                Friendly, Positive
el-GR-NestorasNeural               Male      General                Friendly, Positive
en-AU-NatashaNeural                Female    General                Friendly, Positive
en-AU-WilliamNeural                Male      General                Friendly, Positive
en-CA-ClaraNeural                  Female    General                Friendly, Positive
en-CA-LiamNeural                   Male      General                Friendly, Positive
en-GB-LibbyNeural                  Female    General                Friendly, Positive
en-GB-MaisieNeural                 Female    General                Friendly, Positive
en-GB-RyanNeural                   Male      General                Friendly, Positive
en-GB-SoniaNeural                  Female    General                Friendly, Positive
en-GB-ThomasNeural                 Male      General                Friendly, Positive
en-HK-SamNeural                    Male      General                Friendly, Positive
en-HK-YanNeural                    Female    General                Friendly, Positive
en-IE-ConnorNeural                 Male      General                Friendly, Positive
en-IE-EmilyNeural                  Female    General                Friendly, Positive
en-IN-NeerjaExpressiveNeural       Female    General                Friendly, Positive
en-IN-NeerjaNeural                 Female    General                Friendly, Positive
en-IN-PrabhatNeural                Male      General                Friendly, Positive
en-KE-AsiliaNeural                 Female    General                Friendly, Positive
en-KE-ChilembaNeural               Male      General                Friendly, Positive
en-NG-AbeoNeural                   Male      General                Friendly, Positive
en-NG-EzinneNeural                 Female    General                Friendly, Positive
en-NZ-MitchellNeural               Male      General                Friendly, Positive
en-NZ-MollyNeural                  Female    General                Friendly, Positive
en-PH-JamesNeural                  Male      General                Friendly, Positive
en-PH-RosaNeural                   Female    General                Friendly, Positive
en-SG-LunaNeural                   Female    General                Friendly, Positive
en-SG-WayneNeural                  Male      General                Friendly, Positive
en-TZ-ElimuNeural                  Male      General                Friendly, Positive
en-TZ-ImaniNeural                  Female    General                Friendly, Positive
en-US-AnaNeural                    Female    Cartoon, Conversation  Cute
en-US-AndrewMultilingualNeural     Male      Conversation, Copilot  Warm, Confident, Authentic, Honest
en-US-AndrewNeural                 Male      Conversation, Copilot  Warm, Confident, Authentic, Honest
en-US-AriaNeural                   Female    News, Novel            Positive, Confident
en-US-AvaMultilingualNeural        Female    Conversation, Copilot  Expressive, Caring, Pleasant, Friendly
en-US-AvaNeural                    Female    Conversation, Copilot  Expressive, Caring, Pleasant, Friendly
en-US-BrianMultilingualNeural      Male      Conversation, Copilot  Approachable, Casual, Sincere
en-US-BrianNeural                  Male      Conversation, Copilot  Approachable, Casual, Sincere
en-US-ChristopherNeural            Male      News, Novel            Reliable, Authority
en-US-EmmaMultilingualNeural       Female    Conversation, Copilot  Cheerful, Clear, Conversational
en-US-EmmaNeural                   Female    Conversation, Copilot  Cheerful, Clear, Conversational
en-US-EricNeural                   Male      News, Novel            Rational
en-US-GuyNeural                    Male      News, Novel            Passion
en-US-JennyNeural                  Female    General                Friendly, Considerate, Comfort
en-US-MichelleNeural               Female    News, Novel            Friendly, Pleasant
en-US-RogerNeural                  Male      News, Novel            Lively
en-US-SteffanNeural                Male      News, Novel            Rational
en-ZA-LeahNeural                   Female    General                Friendly, Positive
en-ZA-LukeNeural                   Male      General                Friendly, Positive
es-AR-ElenaNeural                  Female    General                Friendly, Positive
es-AR-TomasNeural                  Male      General                Friendly, Positive
es-BO-MarceloNeural                Male      General                Friendly, Positive
es-BO-SofiaNeural                  Female    General                Friendly, Positive
es-CL-CatalinaNeural               Female    General                Friendly, Positive
es-CL-LorenzoNeural                Male      General                Friendly, Positive
es-CO-GonzaloNeural                Male      General                Friendly, Positive
es-CO-SalomeNeural                 Female    General                Friendly, Positive
es-CR-JuanNeural                   Male      General                Friendly, Positive
es-CR-MariaNeural                  Female    General                Friendly, Positive
es-CU-BelkysNeural                 Female    General                Friendly, Positive
es-CU-ManuelNeural                 Male      General                Friendly, Positive
es-DO-EmilioNeural                 Male      General                Friendly, Positive
es-DO-RamonaNeural                 Female    General                Friendly, Positive
es-EC-AndreaNeural                 Female    General                Friendly, Positive
es-EC-LuisNeural                   Male      General                Friendly, Positive
es-ES-AlvaroNeural                 Male      General                Friendly, Positive
es-ES-ElviraNeural                 Female    General                Friendly, Positive
es-ES-XimenaNeural                 Female    General                Friendly, Positive
es-GQ-JavierNeural                 Male      General                Friendly, Positive
es-GQ-TeresaNeural                 Female    General                Friendly, Positive
es-GT-AndresNeural                 Male      General                Friendly, Positive
es-GT-MartaNeural                  Female    General                Friendly, Positive
es-HN-CarlosNeural                 Male      General                Friendly, Positive
es-HN-KarlaNeural                  Female    General                Friendly, Positive
es-MX-DaliaNeural                  Female    General                Friendly, Positive
es-MX-JorgeNeural                  Male      General                Friendly, Positive
es-NI-FedericoNeural               Male      General                Friendly, Positive
es-NI-YolandaNeural                Female    General                Friendly, Positive
es-PA-MargaritaNeural              Female    General                Friendly, Positive
es-PA-RobertoNeural                Male      General                Friendly, Positive
es-PE-AlexNeural                   Male      General                Friendly, Positive
es-PE-CamilaNeural                 Female    General                Friendly, Positive
es-PR-KarinaNeural                 Female    General                Friendly, Positive
es-PR-VictorNeural                 Male      General                Friendly, Positive
es-PY-MarioNeural                  Male      General                Friendly, Positive
es-PY-TaniaNeural                  Female    General                Friendly, Positive
es-SV-LorenaNeural                 Female    General                Friendly, Positive
es-SV-RodrigoNeural                Male      General                Friendly, Positive
es-US-AlonsoNeural                 Male      General                Friendly, Positive
es-US-PalomaNeural                 Female    General                Friendly, Positive
es-UY-MateoNeural                  Male      General                Friendly, Positive
es-UY-ValentinaNeural              Female    General                Friendly, Positive
es-VE-PaolaNeural                  Female    General                Friendly, Positive
es-VE-SebastianNeural              Male      General                Friendly, Positive
et-EE-AnuNeural                    Female    General                Friendly, Positive'''