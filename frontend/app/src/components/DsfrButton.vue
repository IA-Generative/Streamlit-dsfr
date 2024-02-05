<script setup lang="ts">
import { onMounted, onUnmounted, ref, computed } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrButton } from '@gouvminint/vue-dsfr'

import '~/assets/iconify-icon.min.js'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		label?: string | undefined
		secondary?: boolean
		tertiary?: boolean
		disabled?: boolean
		icon?: string | undefined
		iconOnly?: boolean
		iconRight?: boolean
		noOutline?: boolean
		size?: '' | 'small' | 'sm' | 'lg' | 'large' | 'md' | 'medium'
		// Custom props
		link?: string
		copy?: string
	}>
>()

const clicked = ref<boolean>(false)
const disabled = computed(() => clicked.value || props.disabled || props.args.disabled)

function onRenderEvent(_event: Event): void
{
	if (clicked.value)
	{
		clicked.value = false
		Streamlit.setComponentValue(clicked.value)
	}
}

onMounted(() =>
	{
		Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

onUnmounted(() =>
	{
		Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

async function onClick()
{
	if (props.args.link)
	{
		window.open(props.args.link, '_blank')?.focus()
	}
	else if (props.args.copy)
	{
		navigator.clipboard.writeText(props.args.copy)
			.catch(err =>
				{
					console.error('Failed to copy:', err)
				})
	}

	if (clicked.value)
	{
		clicked.value = false
		Streamlit.setComponentValue(clicked.value)

		await new Promise(resolve => setTimeout(resolve, 50))
	}

	clicked.value = true
	Streamlit.setComponentValue(clicked.value)
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
	<div class="component" :style="style" :data-icon-only="props.args.iconOnly ? '' : undefined">
		<DsfrButton
			v-bind="props.args"
			:label="undefined"
			:icon="undefined"
			:iconOnly="undefined"
			:disabled="disabled"
			@click="onClick"
		>
			<template v-if="props.args.icon">
				<iconify-icon :icon="iconToIconify(props.args.icon)"></iconify-icon>
			</template>
			<span v-if="!props.args.iconOnly">
				{{ props.args.label }}
			</span>
		</DsfrButton>
	</div>
</template>

<style scoped>
.component :deep(.fr-btn > span) {
	display: contents;
}
.component[data-icon-only] :deep(.fr-btn) {
	font-size: 1.5em;
}
</style>
