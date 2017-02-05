# python code building class code constructs 
# code 

class MyClass(object):
	def __init__(self, regular, oversub, doubleover):
		self.regular = regular 
		self.oversub = oversub
		self.doubleover = doubleover

class PrivateCloud(MyClass):
	def print_privatecloud(self):
		print 'Private Cloud', self.regular

subscription = MyClass(regular='1', oversub='2', doubleover='3')

print subscription.regular 
print subscription.oversub
print subscription.doubleover

privatesub = PrivateCloud(regular='99', oversub='0', doubleover='0')

privatesub.print_privatecloud()

subscription_cloud = PrivateCloud(regular="A", oversub="B", doubleover="C")

subscription_cloud.print_privatecloud()

