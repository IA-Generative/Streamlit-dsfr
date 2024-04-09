<script setup lang="ts">
import { DsfrButton } from '@gouvminint/vue-dsfr'

import '~/assets/iconify-icon.min.js'

const props = defineProps<{
	label?: string
	type?: 'primary' | 'secondary' | 'tertiary' | 'success' | 'warning' | 'danger'
	disabled?: boolean
	icon?: string
	iconOnly?: boolean
	iconRight?: boolean
	noOutline?: boolean
	size?: '' | 'small' | 'sm' | 'lg' | 'large' | 'md' | 'medium'
	// Custom props
	link?: string
	copy?: string
}>()

const emit = defineEmits<{
	(e: 'click', event: MouseEvent): void
}>()

function onClick(event: MouseEvent): void
{
	if (props.link)
	{
		window.open(props.link, '_blank')?.focus()
	}
	else if (props.copy)
	{
		navigator.clipboard.writeText(props.copy)
			.catch(err =>
				{
					console.error('Failed to copy:', err)
				})
	}

	emit('click', event)
}

function iconToIconify(icon: string | undefined): string | undefined
{
	if (!icon)
	{
		return icon
	}

	// Replace first '-' with ':'
	// E.g. convert 'ri-search-line' to 'ri:search-line'
	return icon.replace('-', ':')
}

</script>

<template>
	<div
		:class="[ 'dsfr-component', `dsfr-button-${props.type || 'primary'}` ]"
		:data-icon-only="props.iconOnly ? '' : undefined"
	>
		<DsfrButton
			v-bind="(props as any)"
			:secondary="props.type === 'secondary'"
			:tertiary="props.type === 'tertiary'"
			:label="undefined"
			:icon="undefined"
			:iconOnly="undefined"
			@click="onClick"
		>
			<template v-if="props.icon">
				<iconify-icon :icon="iconToIconify(props.icon)"></iconify-icon>
			</template>
			<span v-if="!props.iconOnly">
				{{ props.label }}
			</span>
		</DsfrButton>
	</div>
</template>

<style scoped>
.dsfr-component {
	display: contents;
}
.dsfr-component :deep(.fr-btn > span) {
	display: contents;
}
.dsfr-component[data-icon-only] :deep(.fr-btn) {
	padding-inline: .5rem !important;
}
.dsfr-component[data-icon-only] :deep(.fr-btn iconify-icon) {
	font-size: 1.5em;
}

/*
Standard button colors:
- bg-default: rgb(0, 0, 145); #000091
- bg-hover: rgb(18, 18, 255); #1212ff
- bg-active: rgb(35, 35, 255); #2323ff

To compute the other colors,
we use the following formula to balance perceived brightness:
`f(R, G, B) = sqrt( 0.299 * R^2 + 0.587 * G^2 + 0.114 * B^2 )`

Example: To compute the green color for the success button:
We solve `x` for `f(0, x, 0) = f(0, 0, 145)`: `x ~= 64`
*/

.dsfr-component.dsfr-button-success :deep(.fr-btn:not(:disabled):not(:hover):not(:active)) {
	background-color: rgb(0, 64, 0);
}
.dsfr-component.dsfr-button-success :deep(.fr-btn) {
	--hover: rgb(0, 115, 0);
	--active: rgb(0, 120, 0);
}
.dsfr-component.dsfr-button-warning :deep(.fr-btn:not(:disabled):not(:hover):not(:active)) {
	background-color: rgb(74, 37, 0);
}
.dsfr-component.dsfr-button-warning :deep(.fr-btn) {
	--hover: rgb(132, 66, 0);
	--active: rgb(138, 69, 0);
}
.dsfr-component.dsfr-button-danger :deep(.fr-btn:not(:disabled):not(:hover):not(:active)) {
	background-color: rgb(90, 0, 0);
}
.dsfr-component.dsfr-button-danger :deep(.fr-btn) {
	--hover: rgb(160, 0, 0);
	--active: rgb(169, 0, 0);
}
</style>
