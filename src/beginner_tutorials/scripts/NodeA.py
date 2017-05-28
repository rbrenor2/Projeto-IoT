#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String

########## NODE A ###########

pub = rospy.Publisher('NodeA', String, queue_size=10)

mensagemRecebida = None
mensagem = "Minha mensagem numero: "
numeroMensagem = 0
ix = 0
start_time = 0.0
end_time = 0.0
aux_time = 0.0
nomeNode = "node A"


def quandoOuvir(data):
    global numeroMensagem
    if data.data == None:
        novaHash = "%s" % rospy.get_time() + "%s"
        rospy.loginfo("%s", novaHash) 
        print "Ouvido mas com mensagem None!"
        pub.publish(novaHash)
    else:
	global end_time
	end_time = time.time()
	print "End_time %f" % end_time
	str1 = mensagem + "%s" % numeroMensagem
	str2 = data.data
	valido = str1 in str2
	print valido
	if (((end_time - start_time) < 10.0) and valido):         
		print "Ouvido e com mesnagem nao vazia: %s" % data.data
		numeroMensagem += 1
        	novaHash = "%s" % rospy.get_time() + ":" + mensagem + "%s" % numeroMensagem
        	print "Mensagem Enviada para B: %s" % novaHash
        	#Simulando um atraso
        	#Publicando
        	pub.publish(novaHash)
		global start_time
            	start_time = time.time()
	else:		
		novaHash = "%s" % rospy.get_time() + ":" + mensagem + "%s" % numeroMensagem
        	print "Mensagem Enviada para B: %s" % novaHash
        	#Simulando um atraso
        	#Publicando
        	pub.publish(novaHash)
		global start_time
            	start_time = time.time()
		
		
        global start_time
	print "Start_time %f" % start_time
    
    rospy.sleep(1)

def quandoFalar():

    #Cria novo node
    rospy.init_node('NodeA', anonymous=True)
    
    #Seta o rate
    #rate = rospy.Rate(10) # 10hz
    
    #Seta de quem ele vai ouvir as coisas
    rospy.Subscriber('NodeC', String , quandoOuvir)

    while not rospy.is_shutdown():
	#check if its a valid message
	#String com a mensagem recebida e o timestamp de sua geracao para ser repassada ao proximo no
        # 'tempoChegada' + ';' rospy.get_time() + rospy.get_caller_id()

	if ix == 0:
	    
	    novaHash = "%s" % rospy.get_time() + ":" + mensagem + "%s" % numeroMensagem
            print "Mensagem Enviada para B: %s" % novaHash

            #publica nova mensagem para B ouvir
            pub.publish(novaHash)
	    global ix
	    global start_time
	    global aux_time
 		
	    aux_time = time.time()            
	    start_time = time.time()
	    print "Start_time %f" % start_time
	    print "aux_time %f" % aux_time  	
	    
	    while (aux_time - start_time) < 10:
		rospy.sleep(1)
                aux_time = time.time()
		print "aux_time atual %f" % aux_time
	        ix = 1

	    
            ix = 0
        #else:
            #global mensagemRecebida
            #if mensagemRecebida == None:
                #novaHash = "%s" % rospy.get_time()
                #pub.publish(novaHash)
            #else:
                #novaHash = "%s" % rospy.get_time() + "%s" % mensagemRecebida
                #pub.publish(novaHash) 
        

        #rate.sleep()
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        quandoFalar()
    except rospy.ROSInterruptException:
        pass
