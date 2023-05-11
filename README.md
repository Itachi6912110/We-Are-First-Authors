We Are First Authors!
===

## Motivation
Happy to collaborating with others but got embarrassed when discussing about the contribution at last? Flipping coin everytime when no agreement on the author list? Now, everyone can be the FIRST AUTHOR!

## Introduction
To solve the author list issue, some interesting idea for sharing the first author is shown in [Every Author as First Author](https://arxiv.org/abs/2304.01393). Here is another way to make everyone sharing the first author with 2 improvements:

- Decodable: we are able to reconstruct the authors from the combined author name.
- Space-efficient: we are able to combine all the author within the original author-list-like convention (i.e. in line format).

## Usage

### Creating the combined author name

- Using the default script
```
python3 we_are_first_authors.py <name1> <name2> ...
```
It will automatically print out the generated combined author name.

- Using the function API
In your Python code:
```
combined_name = weAreFirstAuthors(<names>)
``` 
where `names` is the list of authors.

### Decoding the original author list

- Using the function API
In your Python code:
```
reconstructed_authors = whoAreWe(<combined_name>)
```

### Have fun, keep peace!