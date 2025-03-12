"""
Lempel-Ziv Prediction (LZP) Compression Algorithm Implementation

The LZP compression algorithm is a dictionary-based compression technique 
that uses contextual prediction to improve compression efficiency.
"""

class LZPCompressor:
    def __init__(self, context_length=8):
        """
        Initialize the LZP compressor.
        
        :param context_length: Length of the context used for prediction (default 8)
        """
        if not isinstance(context_length, int) or context_length <= 0:
            raise ValueError("Context length must be a positive integer")
        
        self.context_length = context_length
    
    def compress(self, data):
        """
        Compress the input data using LZP algorithm.
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data
        """
        # Validate input
        if not data:
            return bytes()
        
        # Convert to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Ensure input is bytes
        if not isinstance(data, bytes):
            raise TypeError("Input must be bytes or string")
        
        compressed = bytearray()
        dictionary = {}
        context = bytes()
        
        for byte in data:
            # Construct the current context
            current_context = context[-self.context_length:]
            
            # Look up the predicted byte based on context
            predicted_key = dictionary.get(current_context)
            
            if predicted_key is not None and predicted_key == byte:
                # If prediction is correct, output a 1-bit flag indicating match
                compressed.append(1)
            else:
                # If prediction is incorrect, output a 0-bit flag and the actual byte
                compressed.append(0)
                compressed.append(byte)
                
                # Update dictionary with new context-byte pair
                dictionary[current_context] = byte
            
            # Update context
            context += bytes([byte])
        
        return bytes(compressed)
    
    def decompress(self, compressed_data):
        """
        Decompress data compressed with the LZP algorithm.
        
        :param compressed_data: Compressed input data
        :return: Decompressed data
        """
        # Validate input
        if not compressed_data:
            return bytes()
        
        # Ensure input is bytes
        if not isinstance(compressed_data, bytes):
            raise TypeError("Compressed data must be bytes")
        
        decompressed = bytearray()
        dictionary = {}
        context = bytes()
        
        i = 0
        while i < len(compressed_data):
            # Get the current context
            current_context = context[-self.context_length:]
            
            # Check the prediction flag
            if compressed_data[i] == 1:
                # Prediction is correct, use predicted byte
                predicted_key = dictionary.get(current_context)
                
                if predicted_key is None:
                    raise ValueError("Decompression error: Invalid compressed data")
                
                byte = predicted_key
                i += 1
            else:
                # Prediction is incorrect, use next byte
                if i + 1 >= len(compressed_data):
                    raise ValueError("Decompression error: Incomplete compressed data")
                
                byte = compressed_data[i + 1]
                i += 2
                
                # Update dictionary with new context-byte pair
                dictionary[current_context] = byte
            
            # Add byte to decompressed data and update context
            decompressed.append(byte)
            context += bytes([byte])
        
        return bytes(decompressed)