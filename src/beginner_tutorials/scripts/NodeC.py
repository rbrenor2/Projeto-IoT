#!/usr/bin/env python

import rospy
from std_msgs.msg import String

########## NODE C ###########

pub = rospy.Publisher('NodeC', String, queue_size=10)

mensagemRecebida = None
nomeNode = "node C"

def quandoOuvir(data):
    if data.data == None:
        print "Nenhuma mensagem recebida"
    else:
        novaHash = "%s" % data.data + ":" + "%s" % rospy.get_time()
        print "Ouvido com mensagem nao vazia: %s" % data.data
        rospy.loginfo("%s", novaHash)
        print "Mensagem Enviada para A: %s" % novaHash
        #Simulando um atraso
        rospy.sleep(10)
        pub.publish(novaHash)
    
    rospy.sleep(5)


def quandoFalar():
    #Cria novo node
    rospy.init_node('NodeC', anonymous=True)
    
    #rate = rospy.Rate(10) # 10hz    

    #Seta de quem ele vai ouvir as coisas
    rospy.Subscriber('NodeB', String, quandoOuvir)
    

    while not rospy.is_shutdown():
	#check if its a valid message
        
	#String com a mensagem recebida e o timestamp de sua geracao para ser repassada ao proximo no
        # 'tempoChegada' + ';' rospy.get_time() + rospy.get_caller_id()
        
        #novaHash = "%s" % rospy.get_time() + ":" + "%s" % mensagemRecebida
        
        #rospy.loginfo("Sou o %s " + "enviando a mensagem: %s", nomeNode, novaHash)

        #publica nova mensagem para B ouvir
        #pub.publish(novaHash)
        #rate.sleep()
        rospy.sleep(5)


if __name__ == '__main__':
    try:
        quandoFalar()
    except rospy.ROSInterruptException:
        pass
