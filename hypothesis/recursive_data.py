from hypothesis import strategies as st
from hypothesis import example

@st.composite
def composite_tree(draw):
    return draw(st.one_of(
        st.booleans(),
        st.tuples(composite_tree(), composite_tree())
    ))


#recursive_tree = st.recursive(
    #st.booleans(), lambda children: st.tuples(children, children),
    #max_leaves=3
#)


recursive_tree = st.recursive(
    st.booleans(), lambda children: st.lists(children, min_size=3)
)


sample_data = {
    u'/Seed/Specification': {
        'attributes': {'Type': ''}
        },
    u'/Seed/Specification/Protein': {
        'attributes': {'Type': u'Time'},
        'input_data': ['05:00:00', '23:30:00', '']
        },
    u'/Retting/Type of Retting': {
        'attributes': {'Type': u'Medium String'},
        'input_data': u'Loreum ipsum...'
    }
}


if __name__ == '__main__':
    #print composite_tree().example()
    print recursive_tree.example()
