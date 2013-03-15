from Vec2 import Vec2 

class AABBox:

	def __init__(self,point=Vec2(),extents=Vec2()):
		self.point=point
		self.extents=extents
	
	def itersectionQuad(self,aabb):
		ycoll=abs(aabb.point.y-self.point.y) <=  (self.extents.y + aabb.extents.y)
		xcoll=abs(aabb.point.x-self.point.x) <=  (self.extents.y + aabb.extents.x)
		return  ycoll and xcoll
	
	def itersectionPoint(self,point):
		ycoll=point.y<=(self.point.y+self.extents.y) and point.y>=(self.point.y-self.extents.y)
		xcoll= point.x<=(self.point.x+self.extents.x) and point.x>=(self.point.x-self.extents.x)
		return ycoll and xcoll
			   
		
		