# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> TODO: 
> * Describe how to execute your program
> * Show the screenshot of using iPerf command in Mininet

After finishing the topology.py, type "./topologt.py" in command line and then you will enter in the Mininet's CLI mode.
Use the following iPerf commands to measure the topology.

![alt text](screenshot2.PNG)
Then you will see the result approximately similar to the following, 
![alt text](screenshot.PNG)
---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail

There are three parts in my code: the class "MyTopo", the function "simpleTest", and main function.

1. MyTopo

   The goal of this class is to build swtiches, hosts, and links. I use the in-built function "addSwitch(name)", "addHost(name)", and addLinks(name,name,bw,delay,loss) to control parameters and fulfill the goal.
   
2. simpleTest()

   In this function, I call the class "MyTopo" to build the topology. Then Create and manage a network with a OvS controller and use TCLink using " net = Mininet( topo = topo, controller = OVSController, link = TCLink)". TCLink means Traffic Control Link. It is necessary so that we can set bandwidth, delay, and loss in a link.
   
   After, start the network by "net.start()" and check connectivity by "net.pingAll()", and then dump every hosts and switches to see the connections by "dumpNodeConnections(net.hosts)" and "dumpNodeConnections(net.switches)".
   Finally, "CLI(net)" means enter in the Mininet's CLI mode.
   
3. main function

   Tell mininet to print useful information by "setLogLevel('info')" and execute the function "simpleTest()".
### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**


2. **Example of Mininet**


3. **Topology Generator**


4. **Measurement**

---
## References

> TODO: 
> * Please add your references in the following

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
    * [mininet.link.TCIntf | Mininet 应用与源码剖析 - yeasy](https://yeasy.gitbooks.io/mininet_book/module_link/tcintf.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [YOUR_NAME](YOUR_GITHUB_LINK)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3
