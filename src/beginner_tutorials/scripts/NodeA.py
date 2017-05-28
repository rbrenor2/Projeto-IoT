#!/usr/bin/env python

import rospy
from std_msgs.msg import String

########## NODE A ###########

pub = rospy.Publisher('NodeA', String, queue_size=10)

mensagemRecebida = None
ix = 0
nomeNode = "node A"


def verificaTempo(data):
    separator = ":"
    #Verifica se a string tem o ":"
    if separator in data:
        #Divide a string e guarda so a parte que o Node A mandou
    	data[4:8]

def quandoOuvir(data):
    if data.data == None:
        novaHash = "%s" % rospy.get_time() + "%s"
        rospy.loginfo("%s", novaHash) 
        print "Ouvido mas com mensagem None!"
        pub.publish(novaHash)
    else:
        print "Ouvido e com mesnagem nao vazia: %s" % data.data
        novaHash = "%s" % rospy.get_time() + ":" + "%s" % data.data
        print "Mensagem Enviada para B: %s" % novaHash
        #Simulando um atraso
        rospy.sleep(5)
        #Publicando
        pub.publish(novaHash)
    
    rospy.sleep(5)

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
	    novaHash = "%s" % rospy.get_time() 
        
            rospy.loginfo("%s", novaHash)

            #publica nova mensagem para B ouvir
            pub.publish(novaHash)
	    global i
            i = 1
        #else:
            #global mensagemRecebida
            #if mensagemRecebida == None:
                #novaHash = "%s" % rospy.get_time()
                #pub.publish(novaHash)
            #else:
                #novaHash = "%s" % rospy.get_time() + "%s" % mensagemRecebida
                #pub.publish(novaHash) 
        

        #rate.sleep()
        rospy.sleep(5)

if __name__ == '__main__':
    try:
        quandoFalar()
    except rospy.ROSInterruptException:
        pass
