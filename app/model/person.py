class Person:
	nama = ""
	nik = ""
	tempat = ""
	tgl_lahir = ""
	prov = ""
	kab = ""
	kec = ""
	kel = ""
	rt = ""
	rw = ""
    
	def to_list(self):
		return [self.nama,self.nik,self.tempat,self.tgl_lahir,self.prov,self.kab,self.kec,self.kel,self.rt,self.rw]

	def to_dict(self):
		return {
			'nama':self.nama,
			'nik':self.nik,
			'tempat':self.tempat,
			'tgl_lahir':self.tgl_lahir,
			'prov':self.prov,
			'kab':self.kab,
			'kec':self.kec,
			'kel':self.kel,
			'kel':self.kel,
			'kel':self.kel,
			'rt':self.rt,
			'rw':self.rw
		}
		
	def get_index():
		return ["nama","nik","tempat","tgl_lahir","prov","kec","kel","rt","rw"]