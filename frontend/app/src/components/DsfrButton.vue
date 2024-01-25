<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
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
const isFocused = ref<boolean>(false)

const onRenderEvent = (_event: Event): void =>
	{
		if (!isFocused.value && clicked.value)
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

const onClick = () =>
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

		if (!clicked.value)
		{
			clicked.value = true
			Streamlit.setComponentValue(clicked.value)
		}
	}

const onFocus = () =>
	{
		isFocused.value = true
	}

const onBlur = () =>
	{
		isFocused.value = false
	}
</script>

<template>
	<div class="component" :style="style">
		<DsfrButton
			v-bind="props.args"
			:label="props.args.label || 'Button'"
			:disabled="props.disabled || props.args.disabled"
			@click="onClick"
			@focus="onFocus"
			@blur="onBlur"
		/>
	</div>
</template>
