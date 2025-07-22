from .._otio import Box2d as Box2d, Clip as Clip, Effect as Effect, ExternalReference as ExternalReference, FreezeFrame as FreezeFrame, Gap as Gap, GeneratorReference as GeneratorReference, ImageSequenceReference as ImageSequenceReference, LinearTimeWarp as LinearTimeWarp, Marker as Marker, MissingReference as MissingReference, SerializableCollection as SerializableCollection, Stack as Stack, TimeEffect as TimeEffect, Timeline as Timeline, Track, Transition as Transition, V2d as V2d
from .schemadef import SchemaDef as SchemaDef

__all__ = ['Box2d', 'Clip', 'Effect', 'TimeEffect', 'LinearTimeWarp', 'ExternalReference', 'FreezeFrame', 'Gap', 'GeneratorReference', 'ImageSequenceReference', 'Marker', 'MissingReference', 'SerializableCollection', 'Stack', 'Timeline', 'Transition', 'SchemaDef', 'timeline_from_clips', 'V2d']

MarkerColor = Marker.Color
TrackKind = Track.Kind
TransitionTypes = Transition.Type
NeighborGapPolicy = Track.NeighborGapPolicy

def timeline_from_clips(clips):
    """Convenience for making a single track timeline from a list of clips."""
