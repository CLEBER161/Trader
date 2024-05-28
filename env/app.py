from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
from pytz import timezone
import time 
import pandas as pd
import pytz
import datetime
import calendar
import requests
import json
from datetime import datetime , timedelta

import urllib.parse
import hmac
import hashlib
import numpy as np

from pandas import json_normalize
from pandas import Series, DataFrame
import warnings
import sys
from sklearn.linear_model import LinearRegression
warnings.filterwarnings('ignore') 
#from mpl_finance import candlestick_ohlc
import pandas as pd


#data_to_ts = lambda x:  calendar.timegm((datetime.datetime.strptime(x, "%d-%m-%Y")).timetuple())
#ts_to_data = lambda x:  datetime.datetime.utcfromtimestamp(x).strftime("%d-%m-%Y")
 
#dataInicial = data_to_ts("18-02-2023")
#dataFinal = data_to_ts("27-02-2023")

import time
import statsmodels.api as sm


#import mplfinance as mpf
import datetime

from pytz import timezone








username=input("Coloque o E-MAIL// ")
password=input("Coloque o passaword do E-MAIL// ")

token = "6207524934:AAEtpYcY443SCD0HJSivf1ShusHhAfwiLkQ"
chat_id= "-657654979"
msg="0"

ativo=input("Coloque o nome do ativo// ")
lotes=int(input("Coloque a quantidade de lotes a ser negociado// "))
#direcao=input("Coloque a opção de compra o venda // Se compra: call, se venda: put// ")
timeframe=int(input("Coloque o tempo grafico// "))

saldo=float(input("Qual o saldo inicial?// "))
tipoCont=input("Tipo de conta PRACTICE ou REAL// ")
#tipoCont="PRACTICE"
quantidade = int(input("Digite a quantidade de MARTIGUELE: "))
t1=int(input("Coloque a primeira faixa de minutos: "))
t2=int(input("Coloque a segunda faixa de minutos: "))
t3=int(input("Coloque a terceira faixa de minutos: "))
t4=int(input("Coloque a quarta faixa de minutos: "))
scr=int(input("Coloque a quantidade de segundos para sicronizar com o relogio da IQ-OPTION: "))
delay=int(input("Coloque um valor de Delay: "))


def FazerConexao(username,password,tipoConta="PRACTICE"):

	# Criar uma instância da API da IQ Option
	api = IQ_Option(username, password)

	# Conectar à API
	api.connect()

	# Colocar a API em modo de prática (conta demo)
	api.change_balance(tipoConta)
	conectado=False
	# Verificar se a conexão foi estabelecida corretamente
	if api.check_connect():
		print("Conexão bem-sucedida!")
		conectado=True 
	else:
		print("Falha na conexão.")
		conectado=False

	# Colocar a API em modo de prática (conta demo)
	return api,conectado

	# Desconectar da API
	#api.close_connect()
#------------------- 
api,conectado = FazerConexao(username,password,tipoConta=tipoCont) 

def timestamp2dataHora(x,timezone_="America/Sao_Paulo"):
	d=datetime.fromtimestamp(x,tz=timezone(timezone_))
	return str(d)









def infosContaIQ(api):
	conta=api.get_profile_ansyc()
	nome=conta["name"]
	moeda=conta["currency"]
	data_criacao= timestamp2dataHora(conta["created"])
	return conta, nome, moeda, data_criacao
    
    


def Dados():
	tempo=time.time()
	candles=[]
	candles=api.get_candles(ativo,60,1000,time.time())
	#candles=api.get_realtime_candles(ativo, 60)
				
		#print (candles.key)
	df = pd.DataFrame(candles)
	df['from']=pd.to_datetime(df['from'],unit='s')
	df['to']=pd.to_datetime(df['to'],unit='s')
	#df = df.rename(columns ='id','from','at','to','open','close','low','high','volume')
	df = df.rename(columns ={'to':'date','min':'low','max':'high'})
	
	df4=df
 
	#print(df1)
	df4['high']=pd.to_numeric(df4["high"])
	df4['low']=pd.to_numeric(df4['low'])
	df4['open']=pd.to_numeric(df4['open'])
	df4['volume']=pd.to_numeric(df4['volume'])
	df4['close']=pd.to_numeric(df4['close'])
	df4['date']=pd.to_numeric(df4['date'])
	#df4['date'] =df4['date'].astype('datetime64[ms]')
	df4['date'] = pd.to_datetime(df4.date)
	df4.set_index('date', inplace=True)
	#print(df4)

	
	return df4




def mh1():
	tempo=time.time()
	candles=[]
	
	candles=api.get_candles(ativo,300,1000,time.time())
	#candles=api.get_realtime_candles(ativo, 60)
	
				
		#print (candles.key)
	df = pd.DataFrame(candles)
	df['from']=pd.to_datetime(df['from'],unit='s')
	df['to']=pd.to_datetime(df['to'],unit='s')
	#df = df.rename(columns ='id','from','at','to','open','close','low','high','volume')
	df = df.rename(columns ={'to':'date','min':'low','max':'high'})
	
	df4=df
 
	#print(df1)
	df4['high']=pd.to_numeric(df4["high"])
	df4['low']=pd.to_numeric(df4['low'])
	df4['open']=pd.to_numeric(df4['open'])
	df4['volume']=pd.to_numeric(df4['volume'])
	df4['close']=pd.to_numeric(df4['close'])
	df4['date']=pd.to_numeric(df4['date'])
	#df4['date'] =df4['date'].astype('datetime64[ms]')
	df4['date'] = pd.to_datetime(df4.date)
	df4.set_index('date', inplace=True)
	df['SMA'] = df4['close'].ewm(span=6, adjust=False).mean()
	df['SMA_between_high_low'] = ((df['SMA'] >= df[['open', 'close']].min(axis=1)) & (df['SMA'] <= df[['open', 'close']].max(axis=1)))
	#df['SMA_between_high_low'] = ((df['SMA'] >= df['low']) & (df['SMA'] <= df['high']))	
 #print(df4)

	#suportes e resistencia
	#suporte = df4['close'].rolling(window=15).min()
	#resistencia = df4['close'].rolling(window=15).max()
	
	#suporte2 = suporte[-1]
	#resistencia2 = resistencia[-1]
	
	#fibonacci
	#def fibonacci_retracement():
		#max_price = resistencia
		#min_price = suporte
		
		#retracement_levels = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]
		
		#retracement_prices = []
		#for level in retracement_levels:
			#retracement_price = max_price - (level * (max_price - min_price))
			#retracement_prices.append(retracement_price)
		
		#return retracement_prices
	
	
	#velasF='A' if df4['open'][-10] < df4['close'][-10] else 'B' if df4['open'][-10] > df4['close'][-10] else 'D'
	#velasE='A' if df4['open'][-9] < df4['close'][-9] else 'B' if df4['open'][-9] > df4['close'][-9] else 'D'
	#velasD='A' if df4['open'][-8] < df4['close'][-8] else 'B' if df4['open'][-8] > df4['close'][-8] else 'D'
	#velasC='A' if df4['open'][-7] < df4['close'][-7] else 'B' if df4['open'][-7] > df4['close'][-7] else 'D'
	#velasB = 'A' if df4['open'][-6] < df4['close'][-6] else 'B' if df4['open'][-6] > df4['close'][-6] else 'D'
	#velasA = 'A' if df4['open'][-5] < df4['close'][-5] else 'B' if df4['open'][-5] > df4['close'][-5] else 'D'
	velas4 = 'A' if df4['open'][-4] < df4['close'][-4]else 'B' if df4['open'][-4] > df4['close'][-4] else 'D'
	velas3 = 'A' if df4['open'][-3] < df4['close'][-3] else 'B' if df4['open'][-3] > df4['close'][-3] else 'D'
	velas2 = 'A' if df4['open'][-2] < df4['close'][-2] else 'B' if df4['open'][-2] > df4['close'][-2] else 'D'
	
	cores = velas4 + ' ' + velas3 + ' ' + velas2
	#cores = velasF + ' ' + velasE+ ' ' + velasD+ ' ' + velasC+ ' ' + velasB+ ' ' + velasA+ ' ' + velas4+ ' ' + velas3+ ' ' + velas2
	direcao2=''
	#if (velas2 == 'A' and velas3 == 'A' and velas4 == 'A' ):
		#direcao2=''
	if cores.count('A') > cores.count('B') and cores.count('D')==0:
		direcao2 = 'put'
	elif cores.count('B') > cores.count('A') and cores.count('D')==0:
		direcao2 = 'call'
	else :
		direcao2 = ''
	
	#retracao=fibonacci_retracement()
	return cores, direcao2,df['SMA_between_high_low'] [-2],df['SMA_between_high_low'] [-2]
	
	

def vela():
	tempo=time.time()
	candles=[]
	
	candles=api.get_candles(ativo,300,1000,time.time())
	#candles=api.get_realtime_candles(ativo, 60)
	
				
		#print (candles.key)
	df = pd.DataFrame(candles)
	df['from']=pd.to_datetime(df['from'],unit='s')
	df['to']=pd.to_datetime(df['to'],unit='s')
	#df = df.rename(columns ='id','from','at','to','open','close','low','high','volume')
	df = df.rename(columns ={'to':'date','min':'low','max':'high'})
	
	df4=df
 
	#print(df1)
	df4['high']=pd.to_numeric(df4["high"])
	df4['low']=pd.to_numeric(df4['low'])
	df4['open']=pd.to_numeric(df4['open'])
	df4['volume']=pd.to_numeric(df4['volume'])
	df4['close']=pd.to_numeric(df4['close'])
	df4['date']=pd.to_numeric(df4['date'])
	#df4['date'] =df4['date'].astype('datetime64[ms]')
	df4['date'] = pd.to_datetime(df4.date)
	df4.set_index('date', inplace=True)
	#print(df4)
	vela=''
	direcao3=''
	v5 =  df.iloc[-2]#ultima
	v4 =  df.iloc[-3]#penultima
	v3 =  df.iloc[-4]#antipenuultima
	v2 =  df.iloc[-5]#
	v1 =  df.iloc[-6]#
	v0 =  df.iloc[-7]
    
    ######### reversaõ de tendencia
	if v4["close"] < v4["open"] and v5["close"] > v5["open"] and v5["open"] < v4["close"] and v5["close"] > v4["open"]:
		vela="engulfing_bullish"
		direcao3='call'
	elif v4["open"] > v4["close"] and v4["open"] == v4["high"] and v4["close"] == v4["low"]  and v5["close"] < v4["low"]:
		vela="gravestone_doji"
		direcao3='put'
        
	elif v5["close"] > v4["close"] and v4["close"] > v3["close"]and v3["close"] > v2["close"]and v2["close"] > v1["close"]:
        # Defina suas próprias regras para o padrão "Dragon Dogi" aqui
        # Exemplo hipotético: se o corpo da vela v5 for maior que o corpo da vela v4, e assim por diante.
		vela="dragon_dogi"
		direcao3='call' 
        
	elif v5["close"] > v4["close"] and v4["close"] > v3["close"]and v3["close"] > v2["close"]and v2["close"] > v1["close"]:

		vela="white_soldiers"
		direcao3='call' 
        
	elif v3["close"] > v3["open"] and v4["close"] < v4["open"] and v4["close"] > v3["open"]and v4["open"] < v3["close"] and v5["close"] < v5["open"] and v5["close"] < v3["open"]:
		vela="three_inside_down"
		direcao3='put' 
        
	elif v3["close"] < v3["open"] and v4["close"] > v4["open"] and v4["close"] > v3["open"] and v4["open"] < v3["close"]  and v5["close"] > v5["open"]  and v5["close"] > v4["close"]and v5["open"] > v4["open"]and v5["open"] < v4["close"]:
		vela="three_outside_up"
		direcao3='call'  
        
	elif v3["close"] < v3["open"]  and v4["close"] > v4["open"] and v4["open"] > v3["close"]  and v4["close"] < v3["open"] and v5["close"] > v5["open"] and v5["close"] > v3["open"]:
		vela="three_inside_up"
		direcao3='call'
        
	elif  v3["close"] > v3["open"]  and v4["close"] < v4["open"]  and v4["close"] < v3["open"]and v4["open"] > v3["high"]and v5["close"] < v5["open"]and v5["open"] < v4["open"] and v5["close"] < v4["close"]  :
		vela="three_outside_down"
		direcao3='put' 
        
	elif v3["close"] < v3["open"]  and v4["close"] > v4["open"]and  v4["close"] < v3["open"]and v5["close"] > v5["close"]and v5["close"] >= v3["open"]: 
		vela="bullish_abandoned_baby"
		direcao3='call' 
        
	elif v3["close"] < v3["open"] and v4["close"] < v4["open"] and v4["open"] < v3["close"] and  v5["close"] > v5["open"] and v5["close"] > v4["open"]:
		vela="morning_star"
		direcao3='put' 
        
	elif v3["close"] < v3["open"] and v4["close"] < v4["open"]  and v5["close"] < v5["open"] and v4["open"] < v3["open"] and v4["close"] < v3["close"] and v5["open"] < v4["open"] and v5["close"] < v4["close"] :
		vela="three_black_crows"
		direcao3='put'  
        
	elif v3["close"] > v3["open"] and v4["close"] > v4["open"]  and v5["close"] > v5["open"] and v4["open"] > v3["open"] and v4["close"]  > v3["close"]  and v5["open"] > v4["open"] and v5["close"] > v4["close"] :
		vela="three_white_soldiers"
		direcao3='call'
        
	elif v3['close']<v3["open"]and v4['close']<v4["open"]and v5['close']<v5["open"]and v4['open']<v3["open"]and v4['close']<v3["close"]and v5['open']<v4["close"]and((v5["open"]-v5["close"]<v4["open"]-v4["close"])):
		vela="bullish_deliberation"
		direcao3='call'
        
	elif v3['close']>v3["open"]and v4['close']>v4["open"]and v4['close']>v4["open"]and v4['open']>v3["open"]and v4['close']>v3["close"]and v5['open']>v4["close"]and((v5["close"]-v5["open"]<v4["close"]-v4["open"])):
		vela="bearish_deliberation"
		direcao3='put'           
        
	elif v4["close"] > v4["open"] and v5["close"] < v5["open"] and v5["close"] < ((v4["open"] + v4["close"]) / 2)  and v5["open"] > v4["close"]:
		vela="dark_cloud_cover"
		direcao3='put'
        
	elif v3["close"] < v3["open"] and v4["close"] > v4["open"] and v4["close"] < v3["close"]and v5["close"] > v5["open"]and (v4['open']<v5['open']<v4['close']) and v5["close"] >= ((v3["open"]-v3["close"])/2):
		vela="two_rabbits"
		direcao3='call' 
        
	elif v3["close"] > v3["open"] and v4["close"] < v4["open"] and v4["close"] > v3["close"]and v5["close"] < v5["open"]and (v4['open']>v5['open']>v4['close']) and v5["close"]<= ((v3["close"]-v3["open"])/2):
		vela="two_crows"
		direcao3='put'
        
	elif  v4["close"] > v4["open"] and v5["close"] < v5["open"] and v5["close"] > v4["open"]  and v5["open"] < v4["open"] :
		vela="bearish_harami"
		direcao3='put'  
        
	elif v4["close"] > v4["open"] and v5["close"] < v5["open"] and v5["open"] < v4["open"]:
		vela="bearish_kicker"
		direcao3='put'
        
	elif v4["close"] < v4["open"] and v5["close"] > v5["open"] and v5["open"] > v4["close"] and v5["close"] < v4["open"] :
		vela="bullish_harami"
		direcao3='call'   
        
	elif v4["close"] < v4["open"] and v5["close"] > v5["open"] and v5["open"] >= v4["open"] :
		vela="bullish_kicker"
		direcao3='call' 
        
	elif v4["close"] < v4["open"] and v5["close"] > v5["open"] and v5["close"]<v4["open"] and v5["close"] > ((v4["open"] + v4["close"]) / 2) :
		vela="piercing_line"
		direcao3='call' 
        
	elif  v5["close"] > v5["open"] and v5["high"] - max(v5["close"], v5["open"]) >= 2 * (v5["open"] - v5["close"])  and v5["open"] - min(v5["close"], v5["open"]) <= 0.01 * (v5["high"] - v5["low"]) :
		vela="hammer"
		direcao3='call'   
        
	elif v5["close"] < v5["open"] and v5["high"] - max(v5["close"], v5["open"]) >= 2 * (v5["open"] - v5["close"])  and v5["open"] - min(v5["close"], v5["open"]) <= 0.01 * (v5["high"] - v5["low"]):
		vela="hanging_man"
		direcao3='put'
        
	elif v5["close"] < v5["open"]  and v5["high"] - max(v5["close"], v5["open"]) >= 2 * (v5["open"] - v5["close"])and v5["open"] - min(v5["close"], v5["open"]) <= 0.01 * (v5["high"] - v5["low"]):
		vela="shooting_star"
		direcao3='put'
        
	elif v5["close"] > v5["open"] and v5["low"] - min(v5["close"], v5["open"]) >= 2 * (v5["open"] - v5["close"])  and v5["open"] - max(v5["close"], v5["open"]) <= 0.01 * (v5["high"] - v5["low"]):
		vela="inverted_hammer"
		direcao3='call'        
          
######## continuação        

        
	elif v3["close"] < v3["open"]and v4["close"] > v4["open"]and v3["open"]==v4["open"] and v5["close"]>v4["high"]:
		vela="bullish_separating_line_cont_Alta"
		direcao3='call'   

	elif v3["close"] > v3["open"]and v4["close"] < v4["open"]and v3["open"]==v4["open"]and v5["close"]<v4["low"] :
		vela="bullish_separating_line_cont_Baixa"
		direcao3='put'   

	elif v2["close"]>v2["open"]and v3["close"]>v3["open"]and v4["close"]<v4["open"]and v3["open"]>v2["close"] and v4["open"]<v3["close"]and v4["close"]<v3["open"] and v5["close"]>v4["high"]: 
		vela="upside_tasuki_gap_cont_Alta"
		direcao3='call'   
        

	elif v2["close"]<v2["open"]and v3["close"]<v3["open"]and v4["close"]>v4["open"]and v3["open"]<v2["close"] and v4["open"]>v3["close"]and v4["close"]>v3["open"] and v5["close"]<v4["low"]: 
		vela="downside_tasuki_gap_cont_Baixa"
		direcao3='put'           
        

	elif v2["close"]>v2["open"]and v3["close"]>v3["open"]and v4["close"]>v4["open"]and v3["open"]>v2["close"] and v4["open"]==v3["open"] and v5["close"]>v4["high"]: 
		vela="bullish_side_by_side_green_lines_cont_Alta"
		direcao3='call'             
     
	elif v2["close"]<v2["open"]and v3["close"]>v3["open"]and v4["close"]>v4["open"]and v3["close"]<v2["close"] and v4["open"]==v3["open"] and v5["close"]<v4["low"]: 
		vela="bearish_side_by_side_green_lines_cont_Alta"
		direcao3='put' 
        
	elif v2["close"]>v2["open"]and v3["close"]<v3["open"]and v4["close"]<v4["open"]and v3["close"]>v2["close"] and v4["open"]==v3["open"] and v5["close"]>v4["high"]: 
		vela="bullish_side_by_side_red_lines_cont_Alta"
		direcao3='call'           
         
	elif v2["close"]<v2["open"]and v3["close"]<v3["open"]and v4["close"]<v4["open"]and v3["open"]<v2["close"] and v4["open"]==v3["open"] and v5["close"]<v4["low"]: 
		vela="bearish_side_by_side_red_lines_cont_Baixa"
		direcao3='put' 
        
	elif v0["close"]>v0["open"]and v1["close"]<v1["open"]and v2["close"]<v2["open"]and v3["close"]<v3["open"]and  (v4["close"]>v4["open"]or v4["close"]<v4["open"]) and v5["close"] > v5["open"] and v1["open"]>v0["close"]and v2["open"]<v1["open"]and v2["close"]<v1["close"] and v4["close"]>=v1["open"]and v5["close"]>v4["high"]: 
		vela="bullish_mat_hold_cont_alta"
		direcao3='call'               

	elif v0["close"]<v0["open"]and v1["close"]>v1["open"]and v2["close"]>v2["open"]and v3["close"]>v3["open"]and  (v4["close"]>v4["open"]or v4["close"]<v4["open"]) and v5["close"] < v5["open"] and v1["open"]<v0["close"]and v2["open"]>v1["open"]and v2["close"]>v1["close"] and v4["close"]<=v1["open"]and v5["close"]<v4["low"]: 
		vela="bearish_mat_hold_cont_Baixa"
		direcao3='put'
        

	elif v2["close"]>v2["open"]and v3["close"]>v3["open"]and v4["close"]>v4["open"]and v5["close"]<v5["open"]and v4["open"]>v3["open"]>v2['open'] and v4["close"]>v3["close"]>v2['close'] and v5["open"]>=v4["high"] and v5["close"]>=v2["open"]: 
		vela="bullish_three-line_strick_cont_Alta"
		direcao3='call'               

	elif v2["close"]<v2["open"]and v3["close"]<v3["open"]and v4["close"]<v4["open"]and v5["close"]>v5["open"]and v4["open"]<v3["open"]<v2['open'] and v4["close"]<v3["close"]<v2['close'] and v5["open"]<=v4["low"] and v5["close"]<=v2["open"]: 
		vela="bearish_three-line_strick_cont_Baixa"
		direcao3='put'        
        
        
        
        
	return vela,direcao3




def payout(par, tipo,  API, timeframe = 1):
	if tipo == 'turbo':
		a = API.get_all_profit()
		return int(100 * a[par]['turbo'])
		
	elif tipo == 'digital':
		API.subscribe_strike_list(par, timeframe)
		while True:
			d = API.get_digital_current_profit(par, timeframe)
			if d != False:
				d = int(d)
				break
			time.sleep(1)
		API.unsubscribe_strike_list(par, timeframe)
		return d



def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)
        
def indicador_RSI(df,window):
  df4['change'] = df4['close'] - df4['close'].shift(1) #Calcular diferença entre fecho 

  df4['gain'] = df4.loc[df4['change']>0,'change'].apply(abs) #Calcular Ganhos
  df4.loc[(df4['gain'].isna()),'gain']= 0 
  df4[0,df4.columns.get_loc('gain')] = np.NaN #df.loc[0,'gain'] = np.NaN


  df4['loss'] = df4.loc[df4['change']<0,'change'].apply(abs) #Calcular Perdas
  df4.loc[(df4['loss'].isna()),'loss']= 0
  df4[0,df4.columns.get_loc('loss')] = np.NaN #df.loc[0,'loss'] = np.NaN

  ########### Average Gain/Loss
  #Normalmente são considerados 14 periodos (neste caso vou usar dias)
  df4['avg_gain'] = df4['gain'].rolling(window).mean()
  df4['avg_loss'] = df4['loss'].rolling(window).mean()

  #não pode ser vetorizado porque é uma formula recursiva
  first = df4['avg_gain'].first_valid_index() #identificar primeiro valor que não seja nulo/na

  for index, row in df.iterrows():
    if index == first: #gravar o primeiro não nulo
      prev_avg_gain = row['avg_gain']
      prev_avg_loss = row['avg_loss']
    elif index > first: #calcular os seguintes (após o não nulo)
      df4.loc[index,'avg_gain']= ((prev_avg_gain*(window -1)) + row['gain'])/window
      prev_avg_gain = df4.loc[index,'avg_gain']

      df4.loc[index,'avg_loss']= ((prev_avg_loss*(window -1)) + row['loss'])/window
      prev_avg_loss = df4.loc[index,'avg_loss']

  #### Compute RS e RSI
  df4[f'RS'] = df4['avg_gain']/df4['avg_loss']
  df4[f'RSI'] = 100 - (100 / (1 + df4[f'RS']))

  #Filter Columns
  lista = df4.columns.to_list()
  matching = [s for s in lista if "RSI" in s]
  sel_col = ['close'] + matching

  return df4[sel_col].copy()        



def stochastic(df4, k_window=8, mma_window=3):
	
	
	df4["high"]=pd.to_numeric(df4["high"])
	df4['low']=pd.to_numeric(df4['low'])
	df4['close']=pd.to_numeric(df4['close'])
	df4['n_highest_high'] = df4["high"].rolling(k_window).max()
	df4['n_lowest_low'] = df4['low'].rolling(k_window).min()
	df4["%K"] =((df4["close"] -df4['n_lowest_low']) / (df4['n_highest_high'] -df4['n_lowest_low'])) * 100
	df4["%D"] = df4['%K'].rolling(mma_window).mean()
	df4["Slow %K"] = df4["%D"]
	df4["Slow %D"] = df4["Slow %K"].rolling(mma_window).mean()
	return df4 




def calculate_atr(df4, window=14):
	
    
    #df['high']=pd.to_numeric(df['high'])
    #df['low']=pd.to_numeric(df['low'])
    #df['close']=pd.to_numeric(df['close'])
    
    
    high = df4['high']
    low = df4['low']
    close = df4['close']
    tr1 = np.maximum(high - low, abs(high - close.shift()))
    tr2 = np.maximum(tr1, abs(low - close.shift()))
    tr3 = np.maximum(tr2, abs(high - low))
    atr = pd.Series(tr3.ewm(span=window, min_periods=window).mean(), name='ATR_' + str(window))
    return atr4

def calculate_stop_loss(df4, window=14, multiplier=3):
    atr = calculate_atr(df4, window)
    stop_loss = df4['close'] - (atr*multiplier)
    
    stop_loss=pd.DataFrame(stop_loss)
    
    return stop_loss.copy






def tendencia():
	df4=Dados()
	df42=Dados()
	df43=Dados()
	# criar uma série temporal de exemplo com valores aleatórios
	#data = df['close']
	df4['media_movel']=df4['close'].rolling(window=2).mean()
	df42['media_movel']=df42['close'].rolling(window=5).mean()
	df43['media_movel']=df43['close'].rolling(window=21).mean()
	#print(df)
	# criar uma série temporal de exemplo com valores aleatórios
	data =  df4['media_movel']
	data2 =  df42['media_movel']
	data3 =  df43['media_movel']
	# criar um índice de datas para a série temporal
	dates = df4.index
	dates2 = df42.index
	dates3 = df43.index
	# criar um dataframe com a série temporal e o índice de datas
	df4 = pd.DataFrame({'date': dates, 'value': data})
	df4=df4[-3:-1]
	df42 = pd.DataFrame({'date': dates2, 'value': data2})
	df42=df42[-6:-1]
	df43 = pd.DataFrame({'date': dates3, 'value': data3})
	df43=df43[-22:-1]
	#print(df)
	# ajustar um modelo de regressão linear à série temporal
	model = LinearRegression().fit(df4.index.values.reshape(-1,1), df4['value'])
	mode2 = LinearRegression().fit(df42.index.values.reshape(-1,1), df42['value'])
	mode3 = LinearRegression().fit(df43.index.values.reshape(-1,1), df43['value'])
	# obter o coeficiente angular da reta de regressão
	trend = model.coef_[0]
	trend2 = mode2.coef_[0]
	trend3 = mode3.coef_[0]
	# imprimir o resultado
	tende=""
	# DETREMINAR  FAIXAS MELHORAS E OPERAR EM MERCADOS INDECISO
	
	if trend >0 and trend2>0:# and trend3>0:
		tende="ALTA"
	elif trend <0 and trend2<0:# and trend3<0:
		tende="BAIXA"
	else:	
		tende="INCONCLUSIVO"
	#elif trend ==0 and trend2==0:
		#tende="indeciso"
	return tende,trend,trend2,trend3

def indSlope(series,n):    
    array_sl = [j*0 for j in range(n-1)]
    for j in range(n,len(series)+1):
        y = series[j-n:j]
        x = np.array(range(n))
        x_sc = (x - x.min())/(x.max() - x.min())
        y_sc = (y - y.min())/(y.max() - y.min())
        x_sc = sm.add_constant(x_sc)
        model = sm.OLS(y_sc,x_sc)
        results = model.fit()
        array_sl.append(results.params[-1])
    slope_angle = (np.rad2deg(np.arctan(np.array(array_sl))))
    
    return np.array(slope_angle)
        
def grafico(df4):
	df4 = df4.tail(10)
	x = df4.index.tolist()
	fig =go.Figure(data=[ ])
	fig = go.Figure(data=[go.Candlestick(x=df4.index,open=df4.open, high=df4.high,low=df4.low, close=df4.close)])
	fig.add_trace(go.Scatter(
        x=x[-1:],
        y=np.array([df4["Lenta_EMA"][-1]]),
        name ='mediaLenta',
        mode="markers", 
        marker_size=10,
        marker = dict(color='blue', symbol = "triangle-down")))
	fig.add_trace(go.Scatter(
        x=x[-1:],
        y=np.array([df4["Rapida_EMA"][-1]]),
        name ='mediaRapida',
        mode="markers", 
        marker_size=10,
        marker = dict(color='red', symbol = "triangle-down")))
	
	return fig.show()
	

	
	
#df4=Dados()
#print(df4)

    
#columns=['date', 'open', 'high', 'low', 'close', 'volume']

#for coluna in df4.columns:
    #print(coluna)

#TED=tendencia()
#df4 = df4.tail(10)
#ANGULO = indSlope(df4['close'],5)
    
#print("A TEDENCIA É ESTA :" + str(TED))

def direcional_MHI(cores):
    direcao = ''
    
    if cores.count('A') > cores.count('B') and cores.count('D')==0:
        direcao = 'put'
    
    if cores.count('B') > cores.count('A') and cores.count('D')==0:
        direcao = 'call'
    return direcao

def stop(lucro, gain, loss):
    if lucro <= -loss:
        print('Atenção: Infelizmente atingimos o Stop Loss !')
        sys.exit() 
    if lucro >= gain:
        print('Atenção: Parabéns você bateu a meta do dia - Stop Gain!')
        sys.exit()

def Martingale(entrada, payout):
    # payout precisa está em percentual: ex 0.9
    aposta = entrada * (1+payout)/payout
    return aposta
    
def stop(lucro, gain, loss):
    if lucro <= -loss:
        print('Atenção: Infelizmente atingimos o Stop Loss !')
        sys.exit() 
    if lucro >= gain:
        print('Atenção: Parabéns você bateu a meta do dia - Stop Gain!')
        sys.exit()   

def esperar_segundo_00():
	#time.sleep(300)
	#while True:
		#d = datetime.datetime.now( tz=timezone('America/Sao_Paulo') )
		#minutos = d.minute
		#minutos =str(minutos)
		#horas = d.hour
		#segundos = d.second
		#minut=int(minutos[-1])
		#if (minut==4)or (minut==9):
			#TED=tendencia()
			#break
		#print(" ESPERANDO O MOMENTO DE ENTRAR ")
		#time.sleep(1)
	pass	


gain  = lotes*2
loss=-1*( lotes*2)

msg="0"
situacao_lucro=0
conts = 1; # contador de segundos
contm = 1
preçoCompra=0
entrar = False
ca=0
cb=0

info = api.get_profile_ansyc()
#++++++++++++++++++++++++++ IMPORTANTISSSSIMO ++++++++++++++++++++++++++++++++++++
quantidade+=1
while True:
	
	
	
	d = datetime.datetime.now( pytz.timezone('America/Sao_Paulo') )+ timedelta(seconds=scr)
	#fuso_horario_sp = pytz.timezone('America/Sao_Paulo')
	#print(fuso_horario_sp)
	#d = datetime.datetime.now(fuso_horario_sp)
	minutos = d.minute
	minutos =str(minutos)
	horas = d.hour
	segundos =int(d.second)
	minut=int(minutos)
	temp=str(minut)+str(segundos)
	print(d)
	cores = mh1()
	print(cores)
	print()
	#print(temp)
	
	
	if  ((minut==t1 or minut==t2 or minut==t3 or minut==t4)):#or (minut==5)) :   #((minut==0)or (minut==2)or (minut==6)or (minut==8)or (minut==10)) :
		lot=lotes
		lotes1=lotes
		l=0
		pay = payout(ativo,'turbo',api)
		#padrão = vela()
		#time.sleep(60)
		cores = mh1()
		d=datetime.datetime.now( pytz.timezone('America/Sao_Paulo') )+ timedelta(seconds=scr)
		print("HORA "+ str(d))
		print(cores)
		print()
		time.sleep(delay)
		
		
		#padrão = vela()
		#print(padrão)
		#direcao=padrão[1]
		#cores = mh1()
		direcao=cores[1]
		#print(direcao)
		
		for i in range(quantidade):

			#pay = payout(ativo,'turbo',api)
			#padrão = vela()
			#cores = mh1()
			#print("HORA "+ str(datetime.datetime.now()))
			#print(cores)
			
			
			
			#padrão = vela()
			
			#cores = mh1()
			#direcao=cores[1]

			if direcao==''or cores[2]==False:
				#
				#direcao=cores[1]
				print("++++++++++++++++++ AS CONDIÇÕES NÃO FORAM ATENDIDAS +++++++++++++++++++++++++")
				print()
			else:
				#grafico(df4)
				#direcao=padrão[1]
					
				status, ID = api.buy(lotes1,ativo,direcao,timeframe)
				situacao_lucro = api.check_win_v3(ID)
				d=datetime.datetime.now( pytz.timezone('America/Sao_Paulo') )+ timedelta(seconds=scr)
				print("HORA DA OPERAÇÃO "+ str(d))
				print("PAYOUT " +str(pay))
				print(situacao_lucro )
				print(cores)
				print()
				#balance = account_info["balance"]
				#currency = account_info["currency"]
				#print(f"Saldo da conta practice: {balance} {currency}")
				msg ="Payout atual ", str(pay), "% Saldo final ", str(saldo)
				#send_message(token, chat_id, msg)
				
				if situacao_lucro>0:
					situacao_lucro = api.check_win_v3(ID)
					
	          
					#balance = info["amount"]
					#currency = float(account_info["currency"])
					#print(f"Saldo da conta practice: {balance} {currency}")
					#msg ="Trade IQ option Payout atual "+ str(pay)+"% Valor Inicial investido: "	+str(lotes) + " Saldo final "+ str(saldo)+" ATIVO INVESTIDO: "+str(ativo)+" PADRÃO DE CANDLE "+str(padrão[0])
					#send_message(token, chat_id, msg)
					print("+++++++++++ SUCESSO +++++++++++++")
					print(cores)
					
					#esperar_segundo_00()
					#TED=tendencia()
					lotes1=0
					l=0
					print()
					break
					
					
				elif situacao_lucro<0:
					
					print("-------------SEM SUCESSO---------------")
					print(cores)
					print()
					#print("lot " + str(lot)) 
					#print("Contador " + str(l))
					if quantidade >=1:
						cores = mh1()
						if cores[3]==True:
							l+=1
					
							lot=lot*l
					
							lotes1 = Martingale(lot, pay/100)
							print(cores)
							print("-------------TENTARÁ NOVAMENTE---------------")
							print("PAYOUT " +str(pay))
							print("Novo lote "+str(lotes1))
							print()
						else:
							print("-------------NÃO FOI ATENDIDA AS CONDIÇÕES PARA MARTIGALE, PROBABILIDADE DE PERCA---------------")
							break
							print()
					#padrão = vela()
					#print(padrão)
					#direcao=cores[1]
				
    
#status, ID = api.buy(lotes,ativo,direcao,timeframe)  # Atenção é SEMPRE BUY



# if status:
    # print(api.check_win_v3(ID))
    # print('\n')
    # #print(api.check_win_v4(ID))

# if status:
    # situacao, lucro = api.check_win_v3(ID)
    # print("Situação = ", situacao, " | Lucro = ", str(lucro))

# # # para operações na digital:

# # status, ID = API.buy_digital_spot(ativo, lotes, direcao, timeframe)

# # isWin, lucro = API.check_win_digital_v2(ID)

# # if lucro > 0:
    # # print('Tivemos um WIN | Lucro de = '+ str(lucro) )
# # else:
    # # print('Tivemos um LOSS | Prejuízo de = '+ str(lucro) )




# print("ok")
# input()

# # if status:
	# # print(api.check_win_v3(ID))
	# # print('/n')
	# # print(api.check_win_v4(ID))
# # if status:
	# # situacao,lucro=api.check_win_v3(ID)
	# # print("Situação )


# #while True:

	# #candles =api.get_candles(ativo,60,3,time.time())
	# #df = pd.DataFrame(candles, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
	# #print(candles ['close'])
# '''


