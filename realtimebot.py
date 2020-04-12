import discord
from discord.ext import commands

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' due to privacy cant give the token

description = '''I am ur health bot'''

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="custom status"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send("I AM UR PERSONAL HEALTH CARE BOT - BAYMAX ")
@bot.command()
async def covid_19(ctx):
    await ctx.send("its a virus stay in home")
@bot.command()
async def fever(ctx):
        await ctx.send("its a condition where ur body's temp. behaves abnormally")
@bot.command()
async def covid19_symptoms(ctx):
        await ctx.send("cold,fever,cough,respiratory problems are symptoms")
@bot.command()
async def doctor_contact(ctx):
    await ctx.send("http://www.doctorsdirectoryindia.com/")
@bot.command()
async def cold(ctx):
        await ctx.send("The common cold is a self-limited contagious disease that can be caused by a number of different types of viruses. The common cold is medically referred to as a viral upper respiratory tract infection. Symptoms of the common cold may include cough, sore throat, low-grade fever, nasal congestion, runny nose, and sneezing")
@bot.command()
async def cold_cure(ctx):
        await ctx.send("https://www.mayoclinic.org/diseases-conditions/common-cold/in-depth/cold-remedies/art-20046403")
@bot.command()
async def cough(ctx):
        await ctx.send("Chronic cough is a cough that persists over time. Chronic cough is not a disease in itself, but rather a symptom of an underlying condition.")
@bot.command()
async def cough_cure(ctx):
        await ctx.send("https://www.medicalnewstoday.com/articles/322394")
@bot.command()
async def heart_attack(ctx):
        await ctx.send("A heart attack is the death of a segment of heart muscle caused by a loss of blood supply. The blood is usually cut off when an artery supplying the heart muscle is blocked by a blood clot. If some of the heart muscle dies, a person experiences chest pain and electrical instability of the heart muscle tissue")
@bot.command()
async def heart_attack_prevention(ctx):
        await ctx.send("https://medlineplus.gov/howtopreventheartdisease.html")
@bot.command()
async def heart_attack_precautions(ctx):
        await ctx.send("https://www.mayoclinic.org/diseases-conditions/heart-disease/in-depth/heart-disease-prevention/art-20046502")
@bot.command()
async def flu(ctx):
        await ctx.send("Influenza, commonly known as the flu, is an infectious disease caused by an influenza virus. Symptoms can be mild to severe. The most common symptoms include: high fever, runny nose, sore throat, muscle and joint pain, headache, coughing, and feeling tired.")
@bot.command()
async def flu_symptoms(ctx):
        await ctx.send("https://www.cdc.gov/flu/symptoms/symptoms.htm")
@bot.command()
async def malaria(ctx):
        await ctx.send("Malaria is a mosquito-borne infectious disease that affects humans and other animals. Malaria causes symptoms that typically include fever, tiredness, vomiting, and headaches")
@bot.command()
async def malaria_symptoms(ctx):
        await ctx.send("https://www.who.int/news-room/fact-sheets/detail/malaria")
@bot.command()
async def malaria_prevention(ctx):
        await ctx.send("http://www.malaria.com/overview/malaria-prevention-control")
@bot.command()
async def malaria_cure(ctx):
        await ctx.send("https://www.who.int/malaria/areas/treatment/en/")
@bot.command()
async def kidney_stone(ctx):
        await ctx.send("https://www.kidneyfund.org/kidney-disease/kidney-problems/kidney-stones/")
@bot.command()
async def kidney_stone_cure(ctx):
        await ctx.send("https://www.mayoclinic.org/diseases-conditions/kidney-stones/diagnosis-treatment/drc-20355759")
@bot.command()
async def stomach_ache(ctx):
        await ctx.send("The most common cause of localized pain is stomach ulcers (open sores on the inner lining of the stomach). Cramp-like pain may be associated with diarrhea, constipation, bloating, or flatulence. ... Colicky pain is a symptom of more severe conditions, such as gallstones or kidney stones.")
@bot.command()
async def stomach_ache_cure(ctx):
        await ctx.send("https://www.healthline.com/health/digestive-health/natural-upset-stomach-remedies")
@bot.command()
async def diabetes(ctx):
        await ctx.send("Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.")

bot.run(TOKEN)
