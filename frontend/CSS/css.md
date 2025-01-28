# CSS
- css stands for cascading style sheet
- for better look for web application
- css can be implemented in the following ways
    - inline css
    - internal css (page level css)
    - external css
---
# CSS properties
## text properties:
- font-family
- font-size
- text-align
- text-decoration
- text-shadow

---
## size properties
- width: px(pixel) / % / res
- height: px(pixel) / % / res

---
background
- background-color
- color
- background-url
- background-size
---
margin
- margin: 20px
    - all sides 20px
- margin: 15px 20px 21px 28px
    - top right bottom left
- margin-top : 15px
- margin-right : 20px
- margin-bottom : 21px
- margin-left : 28px

---

padding
- padding : 20px
    - all sides 20px
- padding : 15px 20px 21px 28px
    - top right bottom left
- padding-top : 15px
- padding-right : 20px
- padding-bottom : 21px
- padding-left : 28px

---
visibility : hidden
---
display
- display : none
- display : inline
- display : inline-block
- display : block
- display : flex
---
float
- float : right
- float : left
- float : center
---
cursor
- cursor : pointer
---
positon
- position : static
- position : absolute
- position : relative
- position : fixed

# types of selectors
- using id selector
    - using `#IdName` symbol.
    - `id="IdName"` inside tag.
- using class selector
    - using `.className` symbol.
    - `class="className"` inside tag.
- using tag based selector
    - using `tagname`
- using groupby selector
    - using two or more selector using `#id1,#id2`
- using universal selector
    - using `*`
    - it will be applicable to entire page

---
# inline css
- inline css can be represnet as we are using css propertires inside the opening tag followed by style attribute.
```html
    <h1 style="background-color: brown; text-align: center; font-family: monospace; color:rgb(249, 249, 249);">using inline css</h1>
```
---
# Internal css or page level css
- if we are using css or css3 properties inside style tag is called as internal css
```html
<style>
    #InternalCss {
        background-color: rgb(2, 142, 11); 
        text-align: center; 
        font-family: monospace; 
        color:rgb(255, 255, 255);
        border: 3px solid black;
        border-radius: 15px;
        font-size: 25px;
        text-transform: uppercase;
    }
</style>
```
---

# External Css
- External css can be represent as if we are creating a saperate file with .css extention and implementing the css and css3 properties then it is said to be external css
- [Example](style.css)
---

# margin 
- css and css3 supports margin properties 
- the main objective of margin is to work on page level operations
- 