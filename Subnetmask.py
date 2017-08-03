
import random

def sub_mask_calc():
    while True:
        #Enter the IP Address
        ip_address = input('Enter the IP Address: ')
        a=ip_address.split('.')
        #Checking for a valid IP Address
        if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
            break
        else:
            print('The address is invalid, please renter it again: \n')
            continue

    #All possible mask values
    masks=[255,254,252,248,240,224,192,128,0]

    while True:
        #Enter the subnet mask
        subnet_mask=input('Enter the subnet mask: ')
        b=subnet_mask.split('.')

        if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
            break
        else:
            print('The masks is invalid: \n')
            continue


    #Algoithm for subnet identification
    #String to Binary
    mask_octets=[]

    for octets in b:
        bin_val=bin(int(octets)).split('b')[1]
        #print(bin_val)

        bin_val=bin_val.ljust(8,'0')
        #print(bin_val)
        mask_octets.append(bin_val)
        print(mask_octets)

    mask=''.join(mask_octets)

    # Counting host bits in the mask and calculating number of hosts/subnet
    no_of_zeros = mask.count("0")
    no_of_ones = 32 - no_of_zeros
    no_of_hosts = abs(2 ** no_of_zeros - 2)

    # Obtaining the wildcard mask
    wildcard_octets = []
    for w_octet in b:
        wild_octet = 255 - int(w_octet)
        wildcard_octets.append(str(wild_octet))
    wildcard_mask='.'.join(wildcard_octets)

    #Converting the IP Address tp binary
    ip_octet=[]

    for ip_oct in a:
        bin_val= bin(int(ip_oct)).split('b')[1]
        bin_val=bin_val.ljust(8,'0')
        ip_octet.append(bin_val)

    ip_add=''.join(ip_octet)


    ##Obtain network address in Binary
    network_add_bin=ip_add[:(no_of_ones)]+'0'*int(no_of_zeros)
    broadcasr_add_bin=ip_add[:(no_of_ones)]+'1'*int(no_of_zeros)

    net_ip_octets = []
    for octet in range(0, 32, 8):
        net_ip_octet = network_add_bin[octet:octet + 8]
        net_ip_octets.append(net_ip_octet)


    net_ip_address = []
    for each_octet in network_add_bin:
        net_ip_address.append(str(int(each_octet, 2)))

    # print (net_ip_address)

    network_address = ".".join(net_ip_address)
    # print (network_address)

    bst_ip_octets = []
    for octet in range(0, 32, 8):
        bst_ip_octet = broadcasr_add_bin[octet:octet + 8]
        bst_ip_octets.append(bst_ip_octet)

    # print (bst_ip_octets)

    bst_ip_address = []
    for each_octet in bst_ip_octets:
        bst_ip_address.append(str(int(each_octet, 2)))

    # print (bst_ip_address)

    broadcast_address = ".".join(bst_ip_address)
    print (broadcast_address)

    # Results for selected IP/mask
    print("\nNetwork address is: %s" % network_address)
    print( "Broadcast address is: %s" % broadcast_address)
    print("Number of valid hosts per subnet: %s" % no_of_hosts)
    print("Wildcard mask: %s" % wildcard_mask)
    print("Mask bits: %s" % no_of_ones)
    print("\n")



    # Generation of random IP in subnet
    while True:
        generate = input("Generate random ip address from subnet? (y/n)").lower()

        if generate == "y":
            generated_ip = []

            # Obtain available IP address in range, based on the difference between octets in broadcast address and network address
            for indexb, oct_bst in enumerate(bst_ip_address):

                for indexn, oct_net in enumerate(net_ip_address):
                    # print indexn, oct_net
                    if indexb == indexn:
                        if oct_bst == oct_net:
                            # Add identical octets to the generated_ip list
                            generated_ip.append(oct_bst)
                        else:
                            # Generate random number(s) from within octet intervals and append to the list
                            generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))


            y_iaddr = ".".join(generated_ip)
            # print y_iaddr

            print("Random IP address is: %s", ".".join(generated_ip))
            print("\n")
            continue

        else:
            print("Ok, bye!\n")
            break



#Calling function
sub_mask_calc()