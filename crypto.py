import binascii
import base64

class Crypto(object):
	@staticmethod
	def hexstr_to_byte(text):
		return bytearray(text.decode('hex'))

	@staticmethod
	def byte_to_base64str(bytes):
		return base64.b64encode(bytes)

	@staticmethod
	def xor(a, b):
		return bytearray(a[i]^b[i] for i in xrange(len(a)))

	@staticmethod
	def byte_to_hexstr(bytes):
		return base64.b16encode(bytes)

	@staticmethod
	def one_char_xor(bytes):
		nums = bytes
		strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
		return max(strings, key=lambda s: s.count(' '))

	@staticmethod
	def repeat_xor(bytes, repeat_bytes):
		l = len(repeat_bytes)
		return bytearray(bytes[i]^repeat_bytes[i%l] for i in xrange(len(bytes)))

	@staticmethod
	def str2byte(text):
		return bytearray(ord(c) for c in text)


def main():    
    # SET1 Convert hex to base64
	s="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	e="SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
	ans=Crypto.byte_to_base64str(Crypto.hexstr_to_byte(s))
	assert(ans == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

	# SET1 Fixed XOR
	a=Crypto.hexstr_to_byte('1c0111001f010100061a024b53535009181c')
	b=Crypto.hexstr_to_byte('686974207468652062756c6c277320657965')
	ans = Crypto.byte_to_hexstr(Crypto.xor(a,b))
	assert(ans == '746865206B696420646F6E277420706C6179')

	# SET1 Repated XOR
	a= Crypto.str2byte("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal")
	b= Crypto.str2byte("ICE")
	ans = Crypto.byte_to_hexstr(Crypto.repeat_xor(a,b))
	assert(ans == "0B3637272A2B2E63622C2E69692A23693A2A3C6324202D623D63343C2A26226324272765272A282B2F20690A652E2C652A3124333A653E2B2027630C692B20283165286326302E27282F")


if __name__ == "__main__":
    main()
