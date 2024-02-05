<script setup lang="ts">
import { DsfrButton } from '@gouvminint/vue-dsfr'

import '~/assets/iconify-icon.min.js'

const props = defineProps<{
	label?: string
	secondary?: boolean
	tertiary?: boolean
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
	<div class="dsfr-component" :data-icon-only="props.iconOnly ? '' : undefined">
		<DsfrButton
			v-bind="(props as any)"
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
</style>
