SELECT ITEM_ID,ITEM_NAME,RARITY
FROM ITEM_INFO
WHERE ITEM_ID in (SELECT IT.ITEM_ID as ITEM_ID
      FROM ITEM_TREE IT left join ITEM_INFO II
      on IT.PARENT_ITEM_ID = II.ITEM_ID
     WHERE RARITY = 'RARE')
ORDER BY ITEM_ID desc