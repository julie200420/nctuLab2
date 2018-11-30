#!/usr/bin/python                                                                            
                                                                                             
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

'''
Single switch connected to n hosts.
'''
class MyTopo(Topo):
    def build(self):
        # Add switches to a topology
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch5 = self.addSwitch('s5')
        switch6 = self.addSwitch('s6')
        switch7 = self.addSwitch('s7')
        # Add the hosts to a topology
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')
        host7 = self.addHost('h7')
        host8 = self.addHost('h8')
        # Add biderection links to a topology
        self.addLink(host1,switch1,bw=12,delay='6ms',loss=2)
        self.addLink(host2,switch1,bw=20,delay='78us',loss=15)
        self.addLink(host2,switch4,bw=23,delay='6ms',loss=10)
        self.addLink(host5,switch4,bw=14,delay='5ms',loss=2)
        self.addLink(host2,switch6,bw=30,delay='1ms',loss=12)
        self.addLink(host7,switch6,bw=8,delay='2ms',loss=3)
        self.addLink(host2,switch2,bw=25,delay='60us',loss=14)
        self.addLink(host3,switch2,bw=30,delay='35us',loss=18)
        self.addLink(host3,switch5,bw=30,delay='95us',loss=20)
        self.addLink(host6,switch5,bw=15,delay='4ms',loss=3)
        self.addLink(host3,switch7,bw=33,delay='87us',loss=10)
        self.addLink(host8,switch7,bw=18,delay='60us',loss=6)
        self.addLink(host3,switch3,bw=35,delay='2ms',loss=17)
        self.addLink(host4,switch3,bw=13,delay='3ms',loss=5)


'''
Create and test a simple network
'''
def simpleTest():
    # Create a topology with 2 hosts and 1 switch
    topo = MyTopo()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Test connectivity by trying to have all nodes ping each other
    print("Testing network connectivity")
    net.pingAll()
    # Dump every hosts' and switches' connections
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)
    # enter in the Mininet's CLI mode
    CLI(net)

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()
