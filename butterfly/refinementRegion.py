from geometry import _BFMesh


class RefinementRegion(_BFMesh):
    """Butterfly refinement region.

    Attributes:
        name: Name as a string (A-Z a-z 0-9 _).
        vertices: A flatten list of (x, y, z) for vertices.
        faceIndices: A flatten list of (a, b, c) for indices for each face.
        normals: A flatten list of (x, y, z) for face normals.
        refinementMode: Refinement mode (0: inside, 1: outside, 2: distance)
    """

    def __init__(self, name, vertices, faceIndices, normals, refinementMode):
        """Init Butterfly geometry."""
        _BFMesh.__init__(self, name, vertices, faceIndices, normals)
        self.refinementMode = refinementMode

    @property
    def isRefinementRegion(self):
        """Return True for Butterfly refinement region."""
        return True

    @property
    def refinementMode(self):
        """Boundary condition."""
        return self.__refinementMode

    @refinementMode.setter
    def refinementMode(self, rm):
        assert hasattr(rm, 'isRefinementMode'), \
            '{} is not a Butterfly refinement mode.'.format(rm)

        self.__refinementMode = rm


class _RefinementMode(object):
    """Base class for refinement modes.

    Inside, outside, distance

    Attributes:
        levels: A list of (x, y) values for levels.
    """

    def __init__(self, levels):
        self.levels = levels

    @property
    def isRefinementMode(self):
        """Return True for Butterfly refinement mode."""
        return True

    @property
    def levels(self):
        """Set and get levels for refinment region."""
        return self.__levels

    @levels.setter
    def levels(self, lev):
        for l in lev:
            assert len(l) == 2, \
                'Length of each level ({}) should be 2.'.format(len(l))

        # sort levels based on first item for distance
        self.__levels = tuple(tuple(l) for l in sorted(lev, key=lambda x: x[0]))

    def toOpenFOAMDict(self):
        """Return data as a dictionary."""
        return {'mode': self.__class__.__name__.lower(),
                'levels': str(self.levels).replace(',', ' ')}

    def ToString(self):
        """Overwrite ToString .NET method."""
        return self.__repr__()

    def __repr__(self):
        """representation."""
        return 'mode: {}, levels: {}'.format(
            self.__class__.__name__.lower(),
            str(self.levels).replace(',', ' '))


class Distance(_RefinementMode):
    """Distance refinement mode.

    Attributes:
        levels: A list of (x, y) values for levels. 'levels' specifies per
            distance to the surface the wanted refinement level.
    """

    pass


class Inside(_RefinementMode):
    """Inside refinement mode.

    Attributes:
        level: Refinement level as an integer. All cells inside the surface get
            refined up to the level. The surface needs to be closed for this to
            be possible.
    """

    def __init__(self, level):
        """Create an Inside RefinementMode."""
        _RefinementMode.__init__(self, ((1e15, int(level)),))

    def __repr__(self):
        """representation."""
        return 'mode: {}, level: {}'.format(
            self.__class__.__name__.lower(), self.levels[0][1])


class Outside(Inside):
    """Outside refinement mode.

    Attributes:
        level: Refinement level as an integer. All cells inside the surface get
            refined up to the level. The surface needs to be closed for this to
            be possible.
    """

    pass
