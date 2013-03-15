
class Vec2:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
		
	def __add__(self,v):
		return Vec2(self.x+v.x,self.y+v.y)
	
	def __iadd__(self,v):
		self.x+=v.x
		self.y+=v.y		
	
	def __sub__(self,v):
		return Vec2(self.x-v.x,self.y-v.y)
		
	def __isub__(self,v):
		self.x-=v.x
		self.y-=v.y		
		
	def __mul__(self,v):
		return Vec2(self.x*v.x,self.y*v.y)
		
	def __imul__(self,v):
		self.x*=v.x
		self.y*=v.y
	
	def __div__(self,v):
		return Vec2(self.x/v.x,self.y/v.y)
		
	def __idiv__(self,v):
		self.x/=v.x
		self.y/=v.y
		
	def __neg__(self,v):
		return Vec2(-self.x,-self.y)
	