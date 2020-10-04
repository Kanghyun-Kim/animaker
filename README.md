# animaker
plt(matplotlib)->PILimage->gif 
make code

## Usage
- Create object
```python
anim = AniMaker()
```
- Draw figure and make snapshot
```python
fig, ax = plt.subplots(figsize=[6,3])
for i in range(x):
    ...
    anim.make_snapshot()
    ...
```

- If you need to pause on a specific image, use num for adding multiple frame.
```python
anim.set_snapshot(num=20);
```

- Finally, make gif
```python
anim.make_gif('out.gif')
```
