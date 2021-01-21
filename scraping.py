import requests
import bs4
import smtplib

#reward already get
already_done = ["The Graph","Band Protocol", "Algorand", "Maker", "Celo", "Compound", "EOS", "Stellar Lumens", "Kyber Network"]

url = "https://www.coinbase.com/fr/earn"

response = requests.get(url); # GET coinbase earn page

if response.status_code: # if page received
   print("Page received ", response.status_code, "\n")
   soup = bs4.BeautifulSoup(response.text, 'html.parser') # make bs object from our page
   currencies = soup.find_all("div", {"class":"CampaignCard__DescriptionContainer-sc-1jdvk4l-6 jHoTyp"})#get div of all currencies of the page

   for cur in currencies:
      crypto_name= cur.find("h3").text # get all crypto name
      cur_span = cur.find("span", {"class":"Common__Normal-gw3xc6-7 CampaignCardCTA__CTADetails-sc-1p0y5oi-1 dtaBOe"}) # get span with the reward amount

      if cur_span and crypto_name not in already_done : # if span with the reward exist print message
          print(crypto_name + " " + cur_span.text)
          print()
          # Send mail to get the reward
      elif crypto_name not in already_done:
          print(crypto_name, "not now.")

else:
   print("HTTP Error: ", response.status_code)
