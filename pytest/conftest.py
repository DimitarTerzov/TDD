import pytest

@pytest.fixture(scope='session')
def image_file(tmpdir_factory):
    img = compute_expensive_image()
    fn = tmpdir_factory.mktmp('data').join('image.png')
    img.save(str(fn))
    return fn
