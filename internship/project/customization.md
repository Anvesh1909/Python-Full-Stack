# Full Customization of django admin 
```python
list_display = ('id','name','price','is_published','created_at','modified_at')
list_display_links = ('id','name')
list_filter = ('price','created_at')
list_editable = ('is_published',)
search_fields  = ('name','price')
ordering = ('price',)
# exclude = ('discription',)
```

---
- employee or student should be in tabular format
- news and ott should be in list view
- food and products should be in card view
---

# creating the templates 
- the base file gets the particular cdns to all the pages extends the base file 
- we need to extend base class to all the files.

### application urls 
- 