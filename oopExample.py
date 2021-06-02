from classTest import Router, Switch
 
rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
rtr2 = Router('isr4221', '16.9.5', '10.10.10.5')
rtr3 = Router('iosV', '15.6.7', '10.10.10.9')
rtr4 = Router('isr4221', '16.9.5', '10.10.10.10')
sw1 = Switch('cat9300', '16.9.5', '10.10.10.8')
sw2 = Switch('cat9300', '16.9.5', '10.10.10.12')

print('Rtr1\n', rtr1.getdesc(), '\n', sep = '')
print('Rtr2\n', rtr2.getdesc(), '\n', sep = '')
print('Rtr3\n', rtr3.getdesc(), '\n', sep='')
print('Rtr4\n', rtr4.getdesc(), '\n', sep='')
print('Swt1\n',sw1.getdesc(), '\n', sep = '')
print('Swt2\n', sw2.getdesc(), '\n', sep='')
