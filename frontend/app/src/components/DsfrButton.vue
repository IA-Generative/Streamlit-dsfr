<script setup lang="ts">
import { ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrButton } from '@gouvminint/vue-dsfr'

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

	await new Promise(resolve => setTimeout(resolve, 50))

	clicked.value = false
	Streamlit.setComponentValue(clicked.value)
}
</script>

<template>
	<div class="component" :style="style">
		<DsfrButton
			v-bind="props.args"
			:label="props.args.label || 'Button'"
			:disabled="props.disabled || props.args.disabled"
			@click="onClick"
		/>
	</div>
</template>
