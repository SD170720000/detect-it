import pandas as pd
import apization as a

data = pd.read_csv('fusers.csv')
# screenNames = data["screen_name"].to_list()
screenNames = ['bsknair1967', 'kanaujiask', 'surajjadhao', 'littlescgii', 'melendezmdvv', 'doylebmwvb', 'burtonskck', 'hollowaylddxc', 'koreyunderwo', 'rogeliotjj', 'ChereTravis', 'MedfordojhLatas', 'RittenhouseobyN', 'Merriweatherdsl', 'GiovannaBerry', 'CoriBeard', 'VanceValenzuel3', 'EnolaMontgomer1', 'TracyPuckett13', 'AnjaCaldwell1', 'LucinaHoover', 'RashidaHorton2', 'JonathonEwing1', 'LorenzaOrr1', 'RobertB60500658', 'WillettaRomero', 'SheldonFoley', 'CeceliaMcknig17', 'RozanneRobinson', 'ErlineRosario', 'ReinaCochran', 'LandonBradford1', 'DanniePeterson1', 'VernonDean2', 'MaudLester1', 'KyraConley1', 'BrennaWeeks2', 'DoloresMckenz13', 'AnnelieseFrankl', 'JewelBailey14', 'MaynardAnderso2', 'AdelaideDejesu2', 'EulahBurton1', 'ChiquitaRosari2', 'HyoZimmerman', 'YolandaHooper7', 'LeesaHood', 'LorinaMacias', 'JacquelynDunl16', 'DarrylHansen3', 'LillieLeonard12', 'KenyettaSutton', 'TheodoreHarmon2', 'DelmerMorris1', 'PearleAtkins1', 'DelilaMerritt1', 'VerdaMarks1', 'DanialCampbell2', 'MaudieMeyer1', 'HarriettHarvey9']
for screenName in screenNames:
    try:
        user = a.api.get_user(screen_name='@'+screenName)
    except:
        screenNames.remove(screenName)
        print(screenName)

print(screenNames)
