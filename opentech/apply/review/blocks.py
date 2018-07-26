from django import forms

from django.utils.translation import ugettext_lazy as _

from wagtail.core.blocks import RichTextBlock

from opentech.apply.review.fields import ScoredAnswerField
from opentech.apply.review.options import RECOMMENDATION_CHOICES
from opentech.apply.stream_forms.blocks import OptionalFormFieldBlock, CharFieldBlock, TextFieldBlock
from opentech.apply.utils.blocks import CustomFormFieldsBlock, MustIncludeFieldBlock
from opentech.apply.utils.options import RICH_TEXT_WIDGET_SHORT


class ScoreFieldBlock(OptionalFormFieldBlock):
    field_class = ScoredAnswerField

    class Meta:
        label = _('Score')
        icon = 'order'


class ReviewMustIncludeFieldBlock(MustIncludeFieldBlock):
    pass


class RecommendationBlock(ReviewMustIncludeFieldBlock):
    name = 'Recommendation'
    description = 'Overall recommendation'
    field_class = forms.ChoiceField

    class Meta:
        icon = 'pick'

    def get_field_kwargs(self, struct_value):
        kwargs = super().get_field_kwargs(struct_value)
        kwargs['choices'] = RECOMMENDATION_CHOICES
        return kwargs


class RecommendationCommentsBlock(ReviewMustIncludeFieldBlock):
    name = 'Comments'
    description = 'Recommendation comments'
    widget = RICH_TEXT_WIDGET_SHORT

    class Meta:
        icon = 'openquote'


class ReviewCustomFormFieldsBlock(CustomFormFieldsBlock):
    char = CharFieldBlock(group=_('Fields'))
    text = TextFieldBlock(group=_('Fields'))
    text_markup = RichTextBlock(group=_('Fields'), label=_('Paragraph'))
    score = ScoreFieldBlock(group=_('Fields'))

    required_blocks = ReviewMustIncludeFieldBlock.__subclasses__()