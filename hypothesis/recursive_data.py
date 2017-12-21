from hypothesis import strategies as st
from hypothesis import example, assume
from string import printable
import datetime

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

data = {
    u'/Seed/Specification/Desaturated/Desaturation': {
        'attributes': {'Group': 'DAT', 'Descr': '', 'Default': '', 'Units': u' ',
                       'Type': u'Small String', 'Order': 2, 'Size': 2},
        'input_data': ['fghdfh', 'fdghdfgh']
        },
    u'/Genome/Chromo 1': {
        'attributes': {'Group': 'DAT', 'Descr': u'Number of chromos', 'Default': u'120',
                       'Units': u'cm', 'Type': u'Integer', 'Order': 1, 'Size': 2},
        'input_data': [120, 120]
        },
    u'/Growth/Growing Year': {
        'attributes': {'Group': 'DAT', 'Descr': u'4 digit year', 'Default': '',
                       'Units': u' ', 'Type': u'Small String', 'Order': 1, 'Size': 1},
        'input_data': u'werwersd'
        },
    u'/Seed/Specification': {
        'attributes': {'Group': 'STD', 'Descr': '', 'Default': '',
                       'Units': '', 'Type': '', 'Order': 1, 'Size': ''}
        },
    u'/Seed/Specification/Saturated': {
        'attributes': {'Group': 'DAT', 'Descr': '', 'Default': u'',
                       'Units': u' ', 'Type': u'Time', 'Order': 2, 'Size': 2},
        'input_data': ['04:04:04', '05:05:05']
        },
    u'/Seed/Specification/Protein': {
        'attributes': {'Group': 'DAT', 'Descr': '', 'Default': u'', 'Units': u' ',
                       'Type': u'Time', 'Order': 1, 'Size': 1},
        'input_data': ['14:14:14']
        }
}


sample = st.dictionaries(
    st.text(printable), st.fixed_dictionaries({
        'attributes': st.fixed_dictionaries({
            'Group': st.text(printable),
            'Descr': st.text(printable),
            'Default': st.text(printable),
            'Units': st.text(printable),
            'Type': st.text(printable) | st.just('Time'),
            'Order': st.integers(),
            'Size': st.integers()
        }),
        'input_data': (st.text(printable) | st.integers() | st.lists(st.text(printable)) |
                       st.lists(st.integers()) | st.lists(st.floats()))
    }), min_size=1
)


@st.composite
def draw_data_dict(draw):
    sample_dict = draw(sample)

    for key in sample_dict.keys():
        if sample_dict[key]['attributes']['Type'] == 'Time':
            value = draw(
                st.lists(st.times().map(lambda time: time.strftime("%H:%M:%S")) |
                st.just(''), min_size=1)
            )
            sample_dict[key]['input_data'] = value

    return sample_dict


if __name__ == '__main__':
    #print composite_tree().example()
    #print recursive_tree.example()
    #print sample.example()
    dict_ = draw_data_dict().example()
    print dict_
    #print sample.example()
