a='''𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 !

✨ Fɪʟᴇ ɴᴀᴍᴇ : 108 - Guidepost of the Camellia.mkv

✨ Fɪʟᴇ ꜱɪᴢᴇ : 92.27 MiB

✨ Dᴏᴡɴʟᴏᴀᴅ : http://ns-file-to-link.herokuapp.com/27838/108+-+Guidepost+of+the+Camellia.mkv?hash=AgADcg

✨ Wᴀᴛᴄʜ : http://ns-file-to-link.herokuapp.com/watch/27838/108+-+Guidepost+of+the+Camellia.mkv?hash=AgADcg

✨ Nᴏᴛᴇ : 𝐋𝐢𝐧𝐤 𝐰𝐢𝐥𝐥 𝐧𝐨𝐭 𝐞𝐱𝐩𝐢𝐫𝐞 𝐮𝐧𝐭𝐢𝐥 𝐈 𝐝𝐞𝐥𝐞𝐭𝐞.

𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 !

✨ Fɪʟᴇ ɴᴀᴍᴇ : 108 - Guidepost of the Camellia.mkv

✨ Fɪʟᴇ ꜱɪᴢᴇ : 92.27 MiB

✨ Dᴏᴡɴʟᴏᴀᴅ : http://ns-file-to-link.herokuapp.com/28003/108+-+Guidepost+of+the+Camellia.mkv?hash=AgADcg

✨ Wᴀᴛᴄʜ : http://ns-file-to-link.herokuapp.com/watch/28003/108+-+Guidepost+of+the+Camellia.mkv?hash=AgADcg

✨ Nᴏᴛᴇ : 𝐋𝐢𝐧𝐤 𝐰𝐢𝐥𝐥 𝐧𝐨𝐭 𝐞𝐱𝐩𝐢𝐫𝐞 𝐮𝐧𝐭𝐢𝐥 𝐈 𝐝𝐞𝐥𝐞𝐭𝐞.'''

# print(a.split('𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 !')[1].split('✨ Dᴏᴡɴʟᴏᴀᴅ :')[1].split('\n')[0])
# print(a.split('𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 !'))
c=[]
for i in a.split('𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 !')[1:]:
    c.append(i.split('✨ Dᴏᴡɴʟᴏᴀᴅ :')[1].split('\n')[0].replace(' ','')+'\n')
    
f=open("download.txt",'w')
f.writelines(c)
f.close()

