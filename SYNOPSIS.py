import pandas as pd
import matplotlib.pyplot as plt
import csv
# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
#REFERENCES:
#CSV'S: https://www.techpowerup.com/
#Python syntax help: https://geeksforgeeks.com/
#IDEAS help: https://www.knowasiak.com/
#Predefined statement as output for easy implementation.
#predefine statements for further use in the program many times
PrintStatement="\n\nHere are the best recent releases, that will be suitable for ALL PURPOSES including Gaming & Editing.\n\n"
wronginput="\n\nYou have given unspecified input. Please give the input again to proceed."
#introduction text for the whole progrram
print("\n\nChatbot : HELLO GUEST! WELCOME TO MY IP PROJECT. \n                       This chatbot is made by Aditya Gaurav as a IP project of class 12th Science CRSKYN; \n                       For helping people to understand more about CPU's, GPU's and there realted things, and help them to buy according to their need.\n")
#Asking the name of the user to feel reliable and increase User Experience.
Name=input("\n\n\nChatbot : Hello buddy! \n                       I would like to know your name to begin.\n                       Enter your name : ")
print("\nYour Input :",Name)

while True:
    #Guiding the user to asnwer based upon the field of his query to go step by step.
    print("\n\nChatbot : Hello", Name,".\n                       HOW MAY I HELP YOU TODAY? \n \n                       Q. Choose your Query Type : \n                       1. Technical Terminologies Guide \n                       2. CPU Buying Guide \n                       3. GPU Buying Guide\n                       4. Visual Representations\n                       5. Edit Data\n                       6. Add SKUs\n                        Enter your answer in number.")

    #predefined the name of the user of thsi chatbot to use it again in the system easily using concatenation.
    Username=(" \n "+ str(Name)+" : ")
    Guide=int(input(Username))

    #using if else statements to check the user inputs & give further steps to solve the doubt.
    if Guide==1:
        print("\n\nChatbot : WHICH TECH TERM YOU WOULD LIKE TO  LEARN MORE ABOUT? Enter number as reply.")
        #Storing user input in variable to compare it later in code and show predefined outputs.
        TECHid=int(input("                       1. Cores\n                       2. Clock Speed\n                       3. CPU Sockets\n                       4. Lithography\n                       5. L3 Cache\n                       6. TDP\n                       7. Memory Type\n                       8. Shaders\n                       9. TOP's\n                       10. ROP's\n\n                       Enter your answer in number. \n"+str(Username)+" Have something to know? Type no.: "))
#Made the experience rich  by layouting the replies and inputs in chatting form just by adding Names of speakers while showing output and showing proper gaps in statements.
        #all information of technical terms taken from wikipedia.
        if TECHid==1:
            print("Chatbot : A CPU core is a CPU’s processor. In the old days, every processor had just one core that could focus on one task at a time. Today, CPUs have been two and 18 cores, each of which can work on a different task. As you can see in our CPU Benchmarks Hierarchy, that can have a huge impact on performance.  A core can work on one task, while another core works a different task, so the more cores a CPU has, the more efficient it is. Many processors, especially those in laptops, have two cores, but some laptop CPUs (known as mobile CPUs), such as Intel’s 8th Generation processors, have four. You should shoot for at least four cores in your machine if you can afford it. Most processors can use a process called simultaneous multithreading or, if it’s an Intel processor, Hyper-threading (the two terms mean the same thing) to split a core into virtual cores, which are called threads. For example, AMD CPUs with four cores use simultaneous multithreading to provide eight threads, and most Intel CPUs with two cores use Hyper-threading to provide four threads. Some apps take better advantage of multiple threads than others. Lightly-threaded apps, like games, don't benefit from a lot of cores, while most video editing and animation programs can run much faster with extra threads.")
        elif TECHid==2:
            print("Chatbot : In general, a higher clock speed means a faster CPU. However, many other factors come into play.Your CPU processes many instructions (low-level calculations like arithmetic) from different programs every second. The clock speed measures the number of cycles your CPU executes per second, measured in GHz (gigahertz). A “cycle” is technically a pulse synchronized by an internal oscillator, but for our purposes, they’re a basic unit that helps understand a CPU’s speed. During each cycle, billions of transistors within the processor open and close. A CPU with a clock speed of 3.2 GHz executes 3.2 billion cycles per second. (Older CPUs had speeds measured in megahertz, or millions of cycles per second.) Sometimes, multiple instructions are completed in a single clock cycle; in other cases, one instruction might be handled over multiple clock cycles. Since different CPU designs handle instructions differently, it’s best to compare clock speeds within the same CPU brand and generation. For example, a CPU with a higher clock speed from five years ago might be outperformed by a new CPU with a lower clock speed, as the newer architecture deals with instructions more efficiently. An X-series Intel® processor might outperform a K-series processor with a higher clock speed, because it splits tasks between more cores and features a larger CPU cache. But within the same generation of CPUs, a processor with a higher clock speed will generally outperform a processor with a lower clock speed across many applications. This is why it’s important to compare processors from the same brand and generation.")
        elif TECHid==3:
            print("Chatbot : A CPU socket is a specific part on a motherboard that is purposely designed to hold a central processing unit (CPU). A CPU socket or CPU slot is designed with thousands of pins or contact points for power and data transfer between the CPU and the rest of the processors on the motherboard. CPU socket designs are commonly found among desktop PCs and workstations. ")
        elif TECHid==4:
            print("Chatbot : In computing, lithography is the process of imprinting patterns onto semiconductors to use in circuits. Photolithography is used to transfer a pattern from a photomask to the surface of a substrate. The first stage is the imposition of a structure on the beam of light, which is passed through a mask and projected onto the silicon wafer. The ‘resist’, which is a coating on the wafer, undergoes chemical changes when exposed to light. The solubility of the material is modified and formed into a stencil through the application of a solvent.")
        elif TECHid==5:
            print("Chatbot : A Level 3 (L3) cache is a specialized cache that that is used by the CPU and is usually built onto the motherboard and, in certain special processors, within the CPU module itself. It works together with the L1 and L2 cache to improve computer performance by preventing bottlenecks due to the fetch and execute cycle taking too long. The L3 cache feeds information to the L2 cache, which then forwards information to the L1 cache. Typically, its memory performance is slower compared to L2 cache, but is still faster than the main memory (RAM).")
        elif TECHid==6:
            print("Chatbot : TDP stands for thermal design power or, depending who you ask, thermal design profile. The TDP number tells you the maximum heat a computer chip, such as a CPU or GPU, can use in watts. It also is often used as a basic indicator of power consumption. More watts equals better performance, but also higher temperatures and more power consumption. PC OEMs can sometimes lower the TDP on a chip to increase battery life on a laptop or raise it up to boost speed.")
        elif TECHid==7:
            print("Chatbot : (Graphics Double Data Rate) GDDR is double data rate (DDR) memory specialized for fast rendering on graphics cards (GPUs). Introduced in 2000, GDDR is the primary graphics RAM in use today. GDDR is technically ""GDDR SDRAM"" and supersedes VRAM and WRAM.\nEach GDDR generation is faster and includes enhancements; however, although based on DDR memory, GDDR versions do not correspond numerically to DDR. For example, GDDR3 was based on DDR2 chips; GDDR5 on DDR3 and so on.\nGDDR6 As of 2020, GDDR6 is the current version providing a 16 Gbps data rate instead of 13 Gbps for GDDR5X and twice that of GDDR5. GDDR6 also supports the same 32-byte read/write access as GDDR5. See GPU, DDR and SGRAM.")
        elif TECHid==8:
            print("Chatbot : In computer graphics, a shader is a type of computer program originally used for shading in 3D scenes (the production of appropriate levels of light, darkness, and color in a rendered image). They now perform a variety of specialized functions in various fields within the category of computer graphics special effects, or else do video post-processing unrelated to shading, or even perform functions unrelated to graphics.\nTraditional shaders calculate rendering effects on graphics hardware with a high degree of flexibility. Most shaders are coded for (and run on) a graphics processing unit (GPU),[1] though this is not a strict requirement. Shading languages are used to program the GPU's rendering pipeline, which has mostly superseded the fixed-function pipeline of the past that only allowed for common geometry transforming and pixel-shading functions; with shaders, customized effects can be used. The position and color (hue, saturation, brightness, and contrast) of all pixels, vertices, and/or textures used to construct a final rendered image can be altered using algorithms defined in a shader, and can be modified by external variables or textures introduced by the computer program calling the shader.")
        elif TECHid==9:
            print("Chatbot : Unlike gigahertz (GHz), which measures a processor’s clock speed, TFLOP is a direct mathematical measurement of a computer’s performance.\nSpecifically, a teraflop refers to a processor’s capability to calculate one trillion floating-point operations per second. Saying something has “6 TFLOPS,” for example, means that its processor setup can handle 6 trillion floating-point calculations every second, on average.")
        elif TECHid==10:
            print("Chatbot : The render output unit, often abbreviated as ""ROP"", and sometimes called (perhaps more properly) raster operations pipeline, is a hardware component in modern graphics processing units (GPUs) and one of the final steps in the rendering process of modern 3D accelerator boards. The pixel pipelines take pixel and texel information and process it, via specific matrix and vector operations, into a final pixel or depth value. This process is called rasterization. The ROPs perform the transactions between the relevant buffers in the local memory – this includes writing or reading values, as well as blending them together. Dedicated antialiasing hardware used to perform hardware-based antialiasing methods like MSAA is contained in ROPs.")
        else:
            print(wronginput)
        
    elif Guide == 2:
        print("\n\nChatbot : WHICH MANUFACTURER'S RECENT CPU DO YOU WANT TO KNOW ABOUT? \n                       Enter number as reply.")
        #Storing user input in variable to compare it later in code and show predefined outputs.
        CPUid=int(input("                       1. AMD \n                       2. Intel \n"+str(Username)))

        if CPUid==1:
            CPUType=int(input("\nChatbot : WHAT IS YOUR CPU GOING TO BE USED FOR?\n                       1. Light Gaming/Office \n                       2. Heavy Gaming/Editing \n                       Enter number as reply.\n"+str(Username)))
            #Storing user input in variable to compare it later in code and show predefined outputs.
            
            if CPUType==1:
                df=pd.read_csv("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUGAMING.csv",names=["Sr.no.","Product Name","Codename","Cores","Clock","Socket","Lithography","L3 Cache","TDP","Released","Approx.Price"])
                print(PrintStatement,df)
            elif CPUType==2:
                df=pd.read_csv("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUEDITING.csv",names=["Sr.no.","Product Name","Codename","Cores","Clock","Socket","Lithography","L3 Cache","TDP","Released","Approx.Price"])
                print(PrintStatement,df)
            else:
                print(wronginput)

            
        elif CPUid==2:
            CPUType=int(input("\nChatbot : WHAT IS YOUR CPU GOING TO BE USED FOR?\n                       1. Light Gaming/Office \n                       2. Heavy Gaming/Editing\n                       Enter number as reply.\n"+str(Username)))
            #Storing user input in variable to compare it later in code and show predefined outputs.
            
            if CPUType==1:
                df=pd.read_csv("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUGAMING.csv",names=["Sr.no.","Product Name","Codename","Cores","Clock","Socket","Lithography","L3 Cache","TDP","Released","Approx.Price"])
                print(PrintStatement,df)
            elif CPUType==2:
                df=pd.read_csv("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUEDITING.csv",names=["Sr.no.","Product Name","Codename","Cores","Clock","Socket","Lithography","L3 Cache","TDP","Released","Approx.Price"])
                print(PrintStatement,df)
            else:
                print(wronginput)
        else:
            print(wronginput)

    elif Guide == 3:
        print("\n\nChatbot : WHICH MANUFACTURER'S RECENT GPU DO YOU WANT TO KNOW ABOUT?\n")
        GPUid=int(input("                       1. AMD\n                       2. Nvidia\n                       Enter number as reply.\n"+str(Username)))
        #Storing user input in variable to compare it later in code and show predefined outputs.
        if GPUid==1:
            df=pd.read_csv("C:\\Users\\Student22\\Desktop\\Python\\AMDGPU.csv",names=["Sr.no.","Product Name","Chip","Released","Bus","Memory","MemoryType","Bus Width","G.Clocks","M,Clocks","Shaders/TMU's/ROP's"])
            print(PrintStatement,df)
        elif GPUid==2:
            df=pd.read_csv("C:\\Users\\Student22\\Desktop\\Python\\NVIDIAGPU.csv",names=["Sr.no.","Product Name","Chip","Released","Bus","Memory","Bus Width","G.Clocks","M,Clocks","Shaders/TMU's/ROP's"])
            print(PrintStatement,df)
        else:
            print(wronginput)

    elif Guide==4:
        print("\nChatbot : Get Virtual Comparison of Products sorted by name & benchmark scores.")
        TESTGPU=int(input("\n                       1. Best GPU in market\n                       2. Best CPU in market\n                       Enter number as reply.\n"+str(Username)))
        #Storing user input in variable to compare it later in code and show predefined outputs.
        if TESTGPU==1:
            df9=pd.read_csv("C:\\Users\\Student22\\Desktop\\Python\\GPUMARKS.csv",names=["GPU Name","Score"])
            df9.set_index('GPU Name').plot()
            plt.title("Best Performing GPU's Data")
            plt.ylabel("Benchmark Scores")
            plt.show()
        elif TESTGPU==2:
            df9=pd.read_csv("C:\\Users\\Student22\\Desktop\\Python\\CPUMARKS.csv",names=["CPU Name","Score"])
            df9.set_index('CPU Name').plot()
            plt.title("Best Performing CPU's Data")
            plt.ylabel("Benchmark Scores")
            plt.show()
        else:
            print(wronginput)
            
    elif Guide==6:
        print("\nChatbot : Choose In Which Directory You Have To Add Data?")
        DataADD=int(input("\n\n                       1. AMD CPU\n                       2. INTEL CPU\n                       3. GPU Nvidia\n                       4. GPU AMD\n                       Enter your answer in number.\n"+str(Username)))
        if DataADD==1:
            CPUEdit=int(input("\nChatbot : WHAT IS YOUR AMD CPU CATEGORY?\n                       1. Light Gaming/Office \n                       2. Heavy Gaming/Editing \n                       Enter number as reply.\n"+str(Username)))
            if CPUEdit==1:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUGAMING.csv","a+",newline='')
                wr=csv.writer(file)
                wr.writerow([])
                REC=[]
                ask='y'
                while ask=='y':
                    SR=input("Enter Sr.No. of Product: ")
                    Product=input("Enter Product Name: ")
                    SKU=input("Enter SKU Name: ")
                    Cores=input("Enter Cores & Threads in no.: ")
                    Clock=input("Enter Clock Speeds in Ghz: ")
                    Socket=input("Enter Socket Code Name: ")
                    Lithography=input("Enter Process Lithography Node in nm: ")
                    Cache=input("Enter L3 Cache size in MB: ")
                    Power=input("Enter Power Usage in Watts: ")
                    Date=input("Enter Product Launch Date: ")
                    NewREC=[SR,Product ,SKU,Cores,Clock,Socket,Lithography,Cache,Power,Date]
                    REC.append(NewREC)
                    ask=input("\nEnter y to continue or any other char to exit")
                for i in REC:
                    wr.writerow(i)
                file.close()

            if CPUEdit==2:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUEDITING.csv","a+",newline='')
                wr=csv.writer(file)
                wr.writerow([])
                REC=[]
                ask='y'
                while ask=='y':
                    SR=input("Enter Sr.No. of Product: ")
                    Product=input("Enter Product Name: ")
                    SKU=input("Enter SKU Name: ")
                    Cores=input("Enter Cores & Threads in no.: ")
                    Clock=input("Enter Clock Speeds in Ghz: ")
                    Socket=input("Enter Socket Code Name: ")
                    Lithography=input("Enter Process Lithography Node in nm: ")
                    Cache=input("Enter L3 Cache size in MB: ")
                    Power=input("Enter Power Usage in Watts: ")
                    Date=input("Enter Product Launch Date: ")
                    NewREC=[SR,Product ,SKU,Cores,Clock,Socket,Lithography,Cache,Power,Date]
                    REC.append(NewREC)
                    ask=input("\nEnter y to continue or any other char to exit")
                for i in REC:
                    wr.writerow(i)
                file.close()
            else:
                print(wronginput)

        if DataADD==2:
            CPUEdit=int(input("\nChatbot : WHAT IS YOUR INTEL CPU CATEGORY?\n                       1. Light Gaming/Office \n                       2. Heavy Gaming/Editing \n                       Enter number as reply.\n"+str(Username)))
            if CPUEdit==1:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUGAMING.csv","a+",newline='')
                wr=csv.writer(file)
                wr.writerow([])
                REC=[]
                ask='y'
                while ask=='y':
                    SR=input("Enter Sr.No. of Product: ")
                    Product=input("Enter Product Name: ")
                    SKU=input("Enter SKU Name: ")
                    Cores=input("Enter Cores & Threads in no.: ")
                    Clock=input("Enter Clock Speeds in Ghz: ")
                    Socket=input("Enter Socket Code Name: ")
                    Lithography=input("Enter Process Lithography Node in nm: ")
                    Cache=input("Enter L3 Cache size in MB: ")
                    Power=input("Enter Power Usage in Watts: ")
                    Date=input("Enter Product Launch Date: ")
                    NewREC=[SR,Product ,SKU,Cores,Clock,Socket,Lithography,Cache,Power,Date]
                    REC.append(NewREC)
                    ask=input("\nEnter y to continue or any other char to exit")
                for i in REC:
                    wr.writerow(i)
                file.close()

            if CPUEdit==2:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUEDITING.csv","a+",newline='')
                wr=csv.writer(file)
                wr.writerow([])
                REC=[]
                ask='y'
                while ask=='y':
                    SR=input("Enter Sr.No. of Product: ")
                    Product=input("Enter Product Name: ")
                    SKU=input("Enter SKU Name: ")
                    Cores=input("Enter Cores & Threads in no.: ")
                    Clock=input("Enter Clock Speeds in Ghz: ")
                    Socket=input("Enter Socket Code Name: ")
                    Lithography=input("Enter Process Lithography Node in nm: ")
                    Cache=input("Enter L3 Cache size in MB: ")
                    Power=input("Enter Power Usage in Watts: ")
                    Date=input("Enter Product Launch Date: ")
                    NewREC=[SR,Product ,SKU,Cores,Clock,Socket,Lithography,Cache,Power,Date]
                    REC.append(NewREC)
                    ask=input("\nEnter y to continue or any other char to exit")
                for i in REC:
                    wr.writerow(i)
                file.close()

            else:
                print(wronginput)

        if DataADD==3:
            file=open("C:\\Users\\Student22\\Desktop\\Python\\NVIDIAGPU.csv","a+",newline='')
            wr=csv.writer(file)
            wr.writerow([])
            REC=[]
            ask='y'
            while ask=='y':
                SR=input("Enter Sr.No. of Product: ")
                Product=input("Enter Product Name: ")
                SKU=input("Enter SKU Name: ")
                Date=input("Enter Product Launch Date: ")
                Cores=input("Enter PCIe Lane ")
                Clock=input("Enter Memory in GB: ")
                Socket=input("Enter RAM Type: ")
                Lithography=input("Enter Bus Width: ")
                Cache=input("Enter G.Clocks: ")
                Power=input("Enter Mem. Clocks: ")
                Tflops=input("Enter Shaders,TMUs,ROPs")
                NewREC=[SR,Product ,SKU,Date,Cores,Clock,Socket,Lithography,Cache,Power,Tflops]
                REC.append(NewREC)
                ask=input("\nEnter y to continue or any other char to exit")
            for i in REC:
                wr.writerow(i)
            file.close()
                
        if DataADD==4:
            file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDGPU.csv","a+",newline='')
            wr=csv.writer(file)
            wr.writerow([])
            REC=[]
            ask='y'
            while ask=='y':
                SR=input("Enter Sr.No. of Product: ")
                Product=input("Enter Product Name: ")
                SKU=input("Enter SKU Name: ")
                Date=input("Enter Product Launch Date: ")
                Cores=input("Enter PCIe Lane ")
                Clock=input("Enter Memory in GB: ")
                Socket=input("Enter RAM Type: ")
                Lithography=input("Enter Bus Width: ")
                Cache=input("Enter G.Clocks: ")
                Power=input("Enter Mem. Clocks: ")
                Tflops=input("Enter Shaders,TMUs,ROPs")
                NewREC=[SR,Product ,SKU,Date,Cores,Clock,Socket,Lithography,Cache,Power,Tflops]
                REC.append(NewREC)
                ask=input("\nEnter y to continue or any other char to exit")
            for i in REC:
                wr.writerow(i)
            file.close()

        
    elif Guide==5:
        print("\nChatbot : Choose Which Data To Edit?")
        DataChange=int(input("\n\n                       1. AMD CPU\n                       2. INTEL CPU\n                       3. GPU Nvidia\n                       4. GPU AMD\n                       5. DELETE Data(can't be reversed)\n                       Enter your answer in number.\n"+str(Username)))
        if DataChange==1:
            CPUEdit=int(input("\nChatbot : WHAT IS YOUR AMD CPU CATEGORY?\n                       1. Light Gaming/Office \n                       2. Heavy Gaming/Editing \n                       Enter number as reply.\n"+str(Username)))


            if CPUEdit==1:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUGAMING.csv","r")
                Reader=csv.reader(file)
                L=[]
                Uroll=int(input("\nEnter The SR.no. of Product to update: \n"))
                Found=False
                for row in Reader:
                    if row[0]==str(Uroll):
                        Found=True
                        Product=input("Enter Product Name: ")
                        row[1]=Product
                        SKU=input("Enter SKU Name: ")
                        row[2]=SKU
                        Cores=input("Enter Cores & Threads in no.: ")
                        row[3]=Cores
                        Clock=input("Enter Clock Speeds in Ghz: ")
                        row[4]=Clock
                        Socket=input("Enter Socket Code Name: ")
                        row[5]=Socket
                        Lithography=input("Enter Process Lithography Node in nm: ")
                        row[6]=Lithography
                        Cache=input("Enter L3 Cache size in MB: ")
                        row[7]=Cache
                        Power=input("Enter Power Usage in Watts: ")
                        row[8]=Power
                        Date=input("Enter Product Launch Date: ")
                        row[9]=Date
                    L.append(row)
                file.close()

                if Found==False:
                    print('Sr.No. of Product not found')
                else:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUGAMING.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()

                    
            if CPUEdit==2:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUEDITING.csv","r")
                Reader=csv.reader(file)
                L=[]
                Uroll=int(input("\nEnter The SR.no. of Product to update: \n"))
                Found=False
                for row in Reader:
                    if row[0]==str(Uroll):
                        Found=True
                        Product=input("Enter Product Name: ")
                        row[1]=Product
                        SKU=input("Enter SKU Name: ")
                        row[2]=SKU
                        Cores=input("Enter Cores & Threads in no.: ")
                        row[3]=Cores
                        Clock=input("Enter Clock Speeds in Ghz: ")
                        row[4]=Clock
                        Socket=input("Enter Socket Code Name: ")
                        row[5]=Socket
                        Lithography=input("Enter Process Lithography Node in nm: ")
                        row[6]=Lithography
                        Cache=input("Enter L3 Cache size in MB: ")
                        row[7]=Cache
                        Power=input("Enter Power Usage in Watts: ")
                        row[8]=Power
                        Date=input("Enter Product Launch Date: ")
                        row[9]=Date
                    L.append(row)
                file.close()

                if Found==False:
                    print('Sr.No. of Product not found')
                else:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUEDITING.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()
                    
        if DataChange==2:
            CPUEdit=int(input("\nChatbot : WHAT IS YOUR INTEL CPU CATEGORY?\n                       1. Light Gaming/Office \n                       2. Heavy Gaming/Editing \n                       Enter number as reply.\n"+str(Username)))
            if CPUEdit==1:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUGAMING.csv","r")
                Reader=csv.reader(file)
                L=[]
                Uroll=int(input("\nEnter The SR.no. of Product to update: \n"))
                Found=False
                for row in Reader:
                    if row[0]==str(Uroll):
                        Found=True
                        Product=input("Enter Product Name: ")
                        row[1]=Product
                        SKU=input("Enter SKU Name: ")
                        row[2]=SKU
                        Cores=input("Enter Cores & Threads in no.: ")
                        row[3]=Cores
                        Clock=input("Enter Clock Speeds in Ghz: ")
                        row[4]=Clock
                        Socket=input("Enter Socket Code Name: ")
                        row[5]=Socket
                        Lithography=input("Enter Process Lithography Node in nm: ")
                        row[6]=Lithography
                        Cache=input("Enter L3 Cache size in MB: ")
                        row[7]=Cache
                        Power=input("Enter Power Usage in Watts: ")
                        row[8]=Power
                        Date=input("Enter Product Launch Date: ")
                        row[9]=Date
                    L.append(row)
                file.close()

                if Found==False:
                    print('Sr.No. of Product not found')
                else:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUGAMING.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()

                    
            if CPUEdit==2:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUEDITING.csv","r")
                Reader=csv.reader(file)
                L=[]
                Uroll=int(input("\nEnter The SR.no. of Product to update: \n"))
                Found=False
                for row in Reader:
                    if row[0]==str(Uroll):
                        Found=True
                        Product=input("Enter Product Name: ")
                        row[1]=Product
                        SKU=input("Enter SKU Name: ")
                        row[2]=SKU
                        Cores=input("Enter Cores & Threads in no.: ")
                        row[3]=Cores
                        Clock=input("Enter Clock Speeds in Ghz: ")
                        row[4]=Clock
                        Socket=input("Enter Socket Code Name: ")
                        row[5]=Socket
                        Lithography=input("Enter Process Lithography Node in nm: ")
                        row[6]=Lithography
                        Cache=input("Enter L3 Cache size in MB: ")
                        row[7]=Cache
                        Power=input("Enter Power Usage in Watts: ")
                        row[8]=Power
                        Date=input("Enter Product Launch Date: ")
                        row[9]=Date
                    L.append(row)
                file.close()

                if Found==False:
                    print('Sr.No. of Product not found')
                else:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUEDITING.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()

        if DataChange==3:
            file=open("C:\\Users\\Student22\\Desktop\\Python\\NVIDIAGPU.csv","r")
            Reader=csv.reader(file)
            L=[]
            Uroll=int(input("\nEnter The SR.no. of Product to update:\n"))
            Found=False
            for row in Reader:
                if row[0]==str(Uroll):
                    Found=True
                    Product=input("Enter Product Name: ")
                    row[1]=Product
                    SKU=input("Enter SKU Name: ")
                    row[2]=SKU
                    Date=input("Enter Product Launch Date: ")
                    row[3]=Date
                    Lane=input("Enter PCIe Lane Count with Gen: ")
                    row[4]=Lane
                    Memory=input("Enter Memory in GB: ")
                    row[5]=Memory
                    Bus=input("Enter Bus WIdth in bits: ")
                    row[6]=Bus
                    Clock=input("Enter Process Graphic Processor Clock Speeds in Mhz: ")
                    row[7]=Clock
                    Tflops=input("Enter Shaders/TMU's/ROP's: ")
                    row[8]=Tflops
                        
                L.append(row)
            file.close()

            if Found==False:
                print('Sr.No. of Product not found')
            else:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\NVIDIAGPU.csv","w+",newline='')
                Writer=csv.writer(file)
                Writer.writerows(L)
                file.seek(0)
                Reader=csv.reader(file)
                for row in Reader:
                    print(row)
                file.close()

            
        if DataChange==4:
            file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDGPU.csv","r")
            Reader=csv.reader(file)
            L=[]
            Uroll=int(input("\nEnter The SR.no. of Product to update: \n"))
            Found=False
            for row in Reader:
                if row[0]==str(Uroll):
                    Found=True
                    Product=input("Enter Product Name: ")
                    row[1]=Product
                    SKU=input("Enter SKU Name: ")
                    row[2]=SKU
                    Date=input("Enter Product Launch Date: ")
                    row[3]=Date
                    Lane=input("Enter PCIe Lane Count with Gen: ")
                    row[4]=Lane
                    Memory=input("Enter Memory in GB: ")
                    row[5]=Memory
                    Bus=input("Enter Bus WIdth in bits: ")
                    row[6]=Bus
                    Clock=input("Enter Process Graphic Processor Clock Speeds in Mhz: ")
                    row[7]=Clock
                    Tflops=input("Enter Shaders/TMU's/ROP's: ")
                    row[8]=Tflops
                        
                L.append(row)
            file.close()

            if Found==False:
                print('Sr.No. of Product not found')
            else:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDGPU.csv","w+",newline='')
                Writer=csv.writer(file)
                Writer.writerows(L)
                file.seek(0)
                Reader=csv.reader(file)
                for row in Reader:
                    print(row)
                file.close()

                
        if DataChange==5:
            print("\nChatbot : Choose Which Data To DELETE?")
            DataDelete=int(input("\n\n                       1. AMD CPU\n                       2. INTEL CPU\n                       3. GPU Nvidia\n                       4. GPU AMD\n                       Enter your answer in number.\n"+str(Username)))
            if DataDelete==1:
                CPUDelete=int(input("\nChatbot : WHAT IS YOUR AMD CPU CATEGORY?\n                       1. Light Gaming/Office \n                       2. Heavy Gaming/Editing \n                       Enter number as reply.\n"+str(Username)))

                if CPUDelete==1:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUGAMING.csv","r")
                    Reader=csv.reader(file)
                    L=[]
                    Uroll=int(input("\nEnter The SR.no. of Product to Delete: \n"))
                    Found=False
                    for row in Reader:
                        if row[0]==str(Uroll):
                            Found=True
                        else:
                            L.append(row)
                    file.close()

                    if Found==False:
                        print('Sr.No. of Product not found')
                    else:
                     file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUEDITING.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()

                if CPUDelete==2:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUGAMING.csv","r")
                    Reader=csv.reader(file)
                    L=[]
                    Uroll=int(input("\nEnter The SR.no. of Product to Delete: \n"))
                    Found=False
                    for row in Reader:
                        if row[0]==str(Uroll):
                            Found=True
                        else:
                            L.append(row)
                    file.close()

                    if Found==False:
                        print('Sr.No. of Product not found')
                    else:
                     file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDCPUEDITING.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()
                    
            if DataDelete==2:
                CPUDelete=int(input("\nChatbot : WHAT IS YOUR INTEL CPU CATEGORY?\n                       1. Light Gaming/Office \n                       2. Heavy Gaming/Editing \n                       Enter number as reply.\n"+str(Username)))

                if CPUDelete==1:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUGAMING.csv","r")
                    Reader=csv.reader(file)
                    L=[]
                    Uroll=int(input("\nEnter The SR.no. of Product to Delete: \n"))
                    Found=False
                    for row in Reader:
                        if row[0]==str(Uroll):
                            Found=True
                        else:
                            L.append(row)
                    file.close()

                    if Found==False:
                        print('Sr.No. of Product not found')
                    else:
                     file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUGAMING.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()

                if CPUDelete==2:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUEDITING.csv","r")
                    Reader=csv.reader(file)
                    L=[]
                    Uroll=int(input("\nEnter The SR.no. of Product to Delete: \n"))
                    Found=False
                    for row in Reader:
                        if row[0]==str(Uroll):
                            Found=True
                        else:
                            L.append(row)
                    file.close()

                    if Found==False:
                        print('Sr.No. of Product not found')
                    else:
                     file=open("C:\\Users\\Student22\\Desktop\\Python\\INTELCPUEDITING.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()

            if DataDelete==3:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\NVIDIAGPU.csv","r")
                Reader=csv.reader(file)
                L=[]
                Uroll=int(input("\nEnter The SR.no. of Product to Delete: \n"))
                Found=False
                for row in Reader:
                    if row[0]==str(Uroll):
                        Found=True
                    else:
                        L.append(row)
                file.close()

                if Found==False:
                    print('Sr.No. of Product not found')
                else:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\NVIDIAGPU.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()

            if DataDelete==4:
                file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDGPU.csv","r")
                Reader=csv.reader(file)
                L=[]
                Uroll=int(input("\nEnter The SR.no. of Product to Delete: \n"))
                Found=False
                for row in Reader:
                    if row[0]==str(Uroll):
                        Found=True
                    else:
                        L.append(row)
                file.close()

                if Found==False:
                    print('Sr.No. of Product not found')
                else:
                    file=open("C:\\Users\\Student22\\Desktop\\Python\\AMDGPU.csv","w+",newline='')
                    Writer=csv.writer(file)
                    Writer.writerows(L)
                    file.seek(0)
                    Reader=csv.reader(file)
                    for row in Reader:
                        print(row)
                    file.close()
            else:
                print(wronginput)
        
        else:
            print(wronginput)
    else:
        print(wronginput)
#Thanks for reading the code, the code copyright belongs to Aditya Gaurav (@TRANSFINIXSKUIX) . +91 83034 34025
