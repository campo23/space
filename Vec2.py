
class Vec2:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
		
	def __add__(self,v):
		if isinstance(v,Vec2):
			return Vec2(self.x+v.x,self.y+v.y)
		else:
			return Vec2(self.x+v,self.y+v)
	
	def __iadd__(self,v):
		if isinstance(v,Vec2):
			self.x+=v.x
			self.y+=v.y		
		else:
			self.x+=v
			self.y+=v
	
	def __sub__(self,v):
		if isinstance(v,Vec2):
			return Vec2(self.x-v.x,self.y-v.y)
		else:
			return Vec2(self.x-v,self.y-v)

	def __isub__(self,v):
		if isinstance(v,Vec2):
			self.x-=v.x
			self.y-=v.y
		else:
			self.x-=v
			self.y-=v
			
	def __mul__(self,v):
		if isinstance(v,Vec2):
			return Vec2(self.x*v.x,self.y*v.y)
		else:
			return Vec2(self.x*v,self.y*v)
			
	def __imul__(self,v):
		if isinstance(v,Vec2):
			self.x*=v.x
			self.y*=v.y
		else:
			self.x*=v
			self.y*=v
			
	def __div__(self,v):
		if isinstance(v,Vec2):
			return Vec2(self.x/v.x,self.y/v.y)
		else:
			return Vec2(self.x/v,self.y/v)

	def __idiv__(self,v):
		if isinstance(v,Vec2):
			self.x/=v.x
			self.y/=v.y
		else:
			self.x/=v
			self.y/=v
		
	def __neg__(self,v):
		return Vec2(-self.x,-self.y)
	