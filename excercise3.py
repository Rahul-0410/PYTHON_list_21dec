# Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_size=len(sample_list)//3

chunk1=sample_list[:chunk_size]
chunk2=sample_list[chunk_size:2*chunk_size]
chunk3=sample_list[2*chunk_size:]
print("Chunk1",chunk1)
print("After resersing it",chunk1[::-1])
print("Chunk2",chunk2)
print("After resersing it",chunk2[::-1])
print("Chunk3",chunk3)
print("After resersing it",chunk3[::-1])